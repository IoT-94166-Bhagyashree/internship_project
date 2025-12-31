## MQTT Communication

MQTT follows a publish–subscribe model.

ESP32 publishes sensor data to MQTT topics:
- env/temperature
- env/humidity
- env/gas

The MQTT broker receives the data, and subscribers
such as BeagleBone Black can consume it.
