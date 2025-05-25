# Raspberry

This repository contains Python scripts for interfacing and communicating with various sensors and devices using a Raspberry Pi. It demonstrates sensor data acquisition using I2C, SPI, and UART protocols, and serial communication with a particulate matter sensor.

## Contents

- **2BME280_I2C.py**  
  Reads environmental data from two BME280 sensors via I2C at different addresses. It outputs temperature, humidity, pressure, and estimated altitude from both sensors simultaneously.

- **I2C_BME280.py**  
  Reads environmental data from a single BME280 sensor over I2C, printing temperature, humidity, pressure, and estimated altitude.

- **mcp.py**  
  Interfaces with an MCP3008 ADC over SPI to read analog signals from two channels (e.g., potentiometer and LDR). Prints raw ADC values and corresponding voltages.  
  *(Note: PWM-related code is included but commented out.)*

- **mcp3008.py**  
  Demonstrates reading from MCP3008 ADC channel 0 and uses the value to control the brightness of an LED via PWM on a Raspberry Pi GPIO pin.

- **pms5003.py**  
  Reads particulate matter data from a PMS5003 sensor via UART serial port. Continuously outputs PM1.0, PM2.5, and PM10 concentrations in μg/m³.

---

## Prerequisites

- Raspberry Pi with Python 3 installed
- `adafruit-circuitpython-bme280` library for BME280 sensor support
- `spidev` Python module for SPI communication
- `RPi.GPIO` Python module for GPIO control and PWM
- `pyserial` Python module for UART serial communication

Install required Python packages with:

```bash
pip3 install adafruit-circuitpython-bme280 spidev RPi.GPIO pyserial
