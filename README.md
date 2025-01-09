# Electronic Targeting System

Our team has developed an innovative collimator – an optical device designed for precise aiming, commonly used in sports and military applications. Unlike other collimators available on the European market, our model features a dynamically adjustable reticle. A ballistic calculator computes the projectile’s trajectory based on the distance to the target (measured by a laser rangefinder), the type of weapon, and the ammunition used, adjusting the hologram’s position accordingly.

The project leverages cutting-edge technologies:

- Raspberry Pi for performance and flexibility,
- Web application for remote data management,
- OLED display,
- Optical system based on mirrors and lenses to create a hologram,
- No mechanical components, ensuring quiet and reliable operation.

Our device stands out for its practicality and innovation. By adopting an interdisciplinary approach, we have integrated electronics, programming, and engineering into a comprehensive solution that delivers precision and efficiency.

[Video demo (in Polish)](https://youtu.be/mxnaJ6cRivI)

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

