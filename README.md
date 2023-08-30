# IIoT_module7
Examples in IIoT workshop Module 7: including Plotly Dash Open Source, Initial State, Node-Red

## Node-Red Example
<img src="https://github.com/JZ2211/IIoT_module7/assets/100505718/2a86ba18-f033-45e5-b4bd-3c83c91c9d1c" width = "400">

Implemented function:
* A mosquitto MQTT server is setup as the broker in a Raspberry Pi.
* BME280 is connected to the Raspberry pi via I2C and publish sensor data periodically via MQTT broker. 
* A local computer is subscribed in MQTT broker to the BME280 messages and the results are displayed via a web app dashboard on the localhost. The data are also saved to a csv file (named after the date).
