# IIoT_module7
Examples for IIoT workshop Module 7: Node-Red, Plotly Dash, and Initial State

## Node-Red Example
<img src="https://github.com/JZ2211/IIoT_module7/assets/100505718/2a86ba18-f033-45e5-b4bd-3c83c91c9d1c" width = "400">

### 📝 Implemented Functions: 
* A mosquitto MQTT server is setup as the broker in a Raspberry Pi.
* BME280 is connected to the Raspberry pi via I2C and publish sensor data periodically via MQTT broker. 
* A local computer is subscribed in MQTT broker to the BME280 messages and the results are displayed via a web app dashboard on the localhost. The data are also saved to a csv file (named after the date).

### 📝 Steps: 
1. Please follow the instructions at https://nodered.org/docs/getting-started/local to install Node-RED in a locall computer, and https://nodered.org/docs/getting-started/raspberrypi for installation in a Raspberry Pi. 

2. Setup the Mosquitto server (MQTT broker) in the Raspberry Pi: https://randomnerdtutorials.com/how-to-install-mosquitto-broker-on-raspberry-pi/

3. Run the example code: 
    - In the Raspberry Pi: Import or copy file ```rpi_flow.json```
    - In the local computer: Import or copy file ```webapp_flow.json```
    - Configure MQTT in/MQTT out nodes in the flows based on your Mosquitto broker configuration
    - Deploy.

The node in the local computer should receive message every 10 seconds. Open ```http://localhost:1880/ui``` in a browswer and you can observe the results.  

## Plotly Dash Example
<img src="https://github.com/JZ2211/IIoT_module7/assets/100505718/6ab75a92-2736-48ae-9c75-e45502d948d1" width="500">

### 📝 Implemented Functions: 
Plot curves based on checked data series. 

### 📝 Steps: 
1. Install Plotly Dash and Pandas in a local computer:
   ```
   pip install pandas
   pip install dash
   ```
3. Run example python code: `dashapp_demo.py`
4. Open URL http://localhost:8050 at a browser.
5. You can select the data series to be displayed. 
