# Raspberry
# Raspberry Pi Projects - GPIO Control

This repository contains Python scripts for controlling hardware connected to a Raspberry Pi. These scripts demonstrate basic input and output (I/O) functionality using buttons and LEDs, as well as controlling LED brightness through code.

## Project Overview

The repository includes four Python scripts that interact with the Raspberry Pi's GPIO pins. These scripts are designed to control LEDs using buttons, toggle their states, and simulate potentiometer control for LED brightness. Below is a description of each file:

### 1. ButtonRead.py

This script monitors a button connected to GPIO4 on the Raspberry Pi. It checks whether the button is pressed or not, providing feedback on the state of the button.

**Hardware setup:**
- One leg of the button is connected to GND.
- The other leg of the button is connected to GPIO4.

**Usage:**
Run this script to check if the button is pressed or not. The state of the button will be displayed in the terminal.

### 2. ControlLedButton.py

This script controls an LED connected to GPIO18 with a button on GPIO17. When the button is pressed, the LED will turn on, and when the button is released, the LED will turn off.

**Hardware setup:**
- Button is connected to GPIO17.
- LED is connected to GPIO18.

**Usage:**
Press the button to turn the LED on, and release it to turn the LED off. The state of the LED will directly correspond to the state of the button.

### 3. LedSwitchButton.py

This script is similar to **ControlLedButton.py**, but with an added twist: pressing the button will toggle the LED state on or off. Each time the button is pressed, the LED will switch its state.

**Hardware setup:**
- Button is connected to GPIO17.
- LED is connected to GPIO18.

**Usage:**
Press the button to toggle the LED on or off. The LED state will change with each button press.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/IrenStepanyan/Raspberry.git
    ```

2. Navigate into the project folder:
    ```bash
    cd Raspberry
    ```

3. Ensure you have the necessary libraries installed:
    - Install the Raspberry Pi GPIO library:
      ```bash
      sudo apt-get install python3-rpi.gpio
      ```

## Usage

To run any of the scripts, use the following command format:

```bash
python3 script_name.py
