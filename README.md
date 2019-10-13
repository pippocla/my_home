# My Home bTicino platform in Home Assistant
The system is functioning with light and temperature.
LIGHT
Show the state of light
Switch ON or OFF pressing the wall trigger or using HA.

TEMPERATURE
It's possible to read for each zone:

the temperature from the probe, 

the set temperature,

the state of the valve

GATEWAY
It's possible to read the data from the gateway bTicino installed:
Gateway Model
Gateway IP
Gateway Firmware
Gateway Uptime


HOW TO INSTALL
Copy all the file under custom_components directory, if not present, create it.
You must have:
custom_components
  my_home
    __init__.py
    light.py
    sensor.py
    manifest.json

System install automatically OpenWeb==0.0.7 from Pypi


HOW TO USE
ad these in your configuration.yaml


#-------------------------------------------
#
#             MY HOME BTicino
#
#-------------------------------------------
my_home:
  host: 'IP address of your Gateway'
  port: 'the port of your Gateway, default 20000'
  password: 'password of your Gateway'
  
  
  if your Gateway do not use password include the IP address of your homeassistant server in the list of authorized IP


#-------------------------------------------
#
#                  SENSOR
#
#-------------------------------------------
sensor:

#  MY HOME BTicino
  - platform: my_home

    devices:
      #Temperature
       - type: 'Temperature'
         Name: 'Temperature for zone A'
         indirizzo: 'zone A address'
       - type: 'SetTemperature'
         Name: 'Set Temperature for zone A'
         indirizzo: 'zone A address'
       - type: 'Valve_State'
         Name: 'State of the valve for zone A'
         indirizzo: 'zone A address'
      #Gateway
       - type: 'Gateway_IP'
         Name: 'Gateway IP'
         indirizzo: ''
       - type: 'Gateway_Model'
         Name: 'Gateway Model'
         indirizzo: ''
       - type: 'Gateway_Firmware'
         Name: 'Gateway Firmware'
         indirizzo: ''
       - type: 'Gateway_Uptime'
         Name: 'Gateway Uptime'
         indirizzo: ''


#-------------------------------------------
#
#                  LIGHT
#
#-------------------------------------------
light:

#  MY HOME BTicino
  - platform: my_home
    scan_interval: 0.5
    devices:
       - name: 'name of the light '
         indirizzo: 'the address on the bus for your light, is the value you set with 2 jumper on the  rele or wall switch es 72, 42 .....'

  


