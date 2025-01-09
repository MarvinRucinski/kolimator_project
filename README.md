# Electronic Targeting System

A shared success with pride on the podium! 🏆

A project that started as an ambitious idea has transformed into a working prototype and won 2nd place at the Team Projects Conference organized by Wrocław University of Science and Technology. Together with the team, we created CTS – a computer-assisted electronic sighting system.

Our solution allows for dynamic correction of the aiming mark, taking into account key weapon and ammunition parameters. We proved that it is possible to create a solid and functional system for a fraction of the market price of premium-class collimators.

I want to thank the team for the collaborative effort, Mateusz Żurawski for his mentoring, and Comarch for supporting this event and us – young innovators! 🚀

[Demo (in Polish)](https://youtu.be/mxnaJ6cRivI)

## Requirements

- Python 3.x
- npm

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/MarvinRucinski/kolimator_project
    cd kolimator_project
    ```

2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Install frontend dependencies:
    ```sh
    cd theme/static_src
    npm install
    ```

4. Run database migrations:
    ```sh
    python manage.py migrate
    ```

## Running

1. Run the Django development server:
    ```sh
    python manage.py runserver
    ```

2. Run TailwindCSS in development mode:
    ```sh
    cd theme/static_src
    npm run dev
    ```

## Features

- Displaying text on the OLED display
- Drawing a reticle on the OLED display
- Handling forms in the web application

## Authors

- [Jakub Wasilewski](https://github.com/wasilewskiJ)
- Piotr Gabrysch
- Franciszek Radziwolski
- [Marvin Ruciński](https://github.com/MarvinRucinski)

