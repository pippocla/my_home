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

Configuring the hub

my_home:
  host: IP address of the gateway es. '123.123.0.1'
  
  port: by default gateway use '20000', but if you use a different one write here
  
  password: if your gateway use a password, otherways include the IP address of your homeassistant server in the list of                  authorized IP

Configuring Light

light:
#  MY HOME BTicino
  - platform: my_home
    scan_interval: 0.5 (update every 0.5 sec)
    devices:
       - name: A name for your light
         indirizzo: the address on the bus for your light, is the value you set with 2 jumper on the  rele or wall switch es 72, 42 .....

        
        
Configuring thermal probe and/or central unit

sensor:
#  MY HOME BTicino
  - platform: my_home

    devices:
      - type: 'Temperature'
        Name: 'T Zona Notte'
        indirizzo: '11'
      - type: 'SetTemperature'
        Name: 'SetT Zona Notte'
        indirizzo: '11'
      - type: 'Valve_State'
        Name: 'Zona Notte'
        indirizzo: '11'
         

    
      type chose between:
      'Temperature' read the temperature of the zone
      'SetTemperature' read the set temperature of the zone
      'Valve_State' read the state of the valve of the zone
      
      - name: A name for your probe or central unit
        indirizzo: the address on the bus for your probe or central unit, is the value you set with 2 jumper on the  probe or central unit wall  es 11, 12 .....
        
Configuring Gatway info (under sensor: inside -platform: my_home)

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


  


