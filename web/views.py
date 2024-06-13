from django.shortcuts import render
import matplotlib
matplotlib.use('Agg')
from py_ballisticcalc import Velocity, Distance, Angular
from py_ballisticcalc import DragModel, TableG7, TableG1, TableG2, TableG5, TableG6, TableG8, TableGI, TableGS
from py_ballisticcalc import Ammo, Unit, PreferredUnits
from py_ballisticcalc import Weapon, Shot, Calculator
from . import models
from django import forms
import json
import os

import io
import base64

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

PreferredUnits.distance = Unit.Meter
PreferredUnits.velocity = Unit.MPS
PreferredUnits.drop = Unit.Meter
PreferredUnits.sight_height = Unit.Centimeter
PreferredUnits.temperature = Unit.Celsius

class ShotForm(forms.Form):
    weapon = forms.ModelChoiceField(queryset=models.Weapon.objects.all(), initial=1)
    ammo = forms.ModelChoiceField(queryset=models.Ammo.objects.all(), initial=1)
    distance = forms.FloatField(initial=100, label='Distance (m)')
    plot = forms.BooleanField(required=False, initial=False, label='Plot')

def read_coordinates(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
            print(f"Read coordinates: {data}")  # Debugging output
            return data.get('x', 0), data.get('y', 0)
    return 0, 0

def write_coordinates(file_path, x, y):
    with open(file_path, 'w') as file:
        data = {'x': x, 'y': y}
        json.dump(data, file)
        print(f"Wrote coordinates: {data}")  # Debugging output

def shot_view(request):
    form = ShotForm()
    info = None
    plot = None

    if request.method == 'POST':
        form = ShotForm(request.POST)

        if form.is_valid():
            weapon_model = form.cleaned_data['weapon']
            ammo_model = form.cleaned_data['ammo']
            distance = form.cleaned_data['distance']

            drag_tables = {
                'G1': TableG1,
                'G7': TableG7,
                'G2': TableG2,
                'G5': TableG5,
                'G6': TableG6,
                'G8': TableG8,
                'GI': TableGI,
                'GS': TableGS,
            }

            dm = DragModel(
                bc=ammo_model.value,
                drag_table=drag_tables[ammo_model.drag_table],
                weight=ammo_model.weight,
                diameter=ammo_model.diameter,
                length=ammo_model.length,
            )

            ammo = Ammo(
                dm=dm,
                mv=Velocity(ammo_model.mv, Velocity.MPS),
            )

            weapon = Weapon(
                sight_height=weapon_model.sight_height,
                twist=weapon_model.twist,
                zero_elevation=weapon_model.zero_look_angle,
            )

            calc = Calculator()
            shot = Shot(
                weapon=weapon,
                ammo=ammo,
            )

            calc.set_weapon_zero(shot, Distance.Meter(weapon_model.zero_distance))

            calc2 = Calculator()
            barrel_elevation = calc2.barrel_elevation_for_target(shot, Distance.Meter(distance))
            shot.relative_angle = Angular.MOA(barrel_elevation.get_in(Angular.MOA) - weapon.zero_elevation.get_in(Angular.MOA))
            moa_shift = round(shot.relative_angle >> Angular.MOA, 2)
            info = f"{moa_shift} MOA UP"

            # Read current coordinates
            coordinates_file = "/home/kolimator/coordinates.json"
            center_x, center_y = 512, 425

            # Calculate pixel shift
            pixel_shift = moa_shift / 0.3448

            # Update coordinates
            new_x = center_x - pixel_shift
            write_coordinates(coordinates_file, new_x, center_y)
            
            if form.cleaned_data['plot']:

                shot_result = calc2.fire(
                    shot=shot,
                    trajectory_range=Distance.Meter(distance*1.5),
                    extra_data=True
                )

                ax = shot_result.plot()

                buf = io.BytesIO()
                plt.savefig(buf, format='png')
                buf.seek(0)
                plot = base64.b64encode(buf.getvalue()).decode('utf-8')
                buf.close()
            

    return render(request, 'web/shot.html', {'form': form, 'plot': plot, 'info': info})

