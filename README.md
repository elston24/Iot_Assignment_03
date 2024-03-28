README.md:

This repository contains code and scripts for a cloud-based IoT system developed as part of an assignment. The system collects data from virtual sensors, communicates via MQTT protocol, and visualizes data using ThingSpeak. MATLAB scripts are used for data analysis.

Steps followed:

Simulating Virtual Sensors: Employed the Wokwi platform to create a virtual IoT device based on ESP32, featuring simulated sensors for temperature, humidity, and CO2 levels. The main.py script was devised to generate randomized sensor data, subsequently transmitted to a ThingSpeak channel.

Configuration of ThingSpeak: Established a ThingSpeak account and configured a dedicated channel to collect data from the virtual sensors. Integration was established between the channel and the simulated IoT device to facilitate seamless data transmission.

MATLAB Data Analysis: Developed two MATLAB scripts to extract and analyze sensor data retrieved from the ThingSpeak channel. These scripts enable the retrieval of both the latest sensor readings and data spanning the past five hours, respectively.

Files:
1. part_a_main.py : Python script for the virtual sensor simulation and data publication.
2. diagram.json : Configuration file for the Wokwi simulator setup.
3. part_b_latest_data.m : Matlab script for retrieving latest sensor data from ThingSpeak.
4. part_c_5hours_data.m : Matlab script for retrieving sensor data from over the last 5 hours.
