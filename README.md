# Beta test for implement My Home bTicino platform in Home Assistant
The system is functioning with light, temperature and switch.
The platform is able to upgrade the state of light also if you press the wall trigger.
For the moment there is a delay between when you turn on or off a light in HA or on the wall trigger and the HA state, but the action on the light is immediate.

HOW TO INSTALL

Create under configuration directory a new directory custom_components,
then copy the file in the same directory they are here.
You must have:
my_home.py
light
  my_home.py
sensor
  my_home.py
switch
  my_home.py

You have to install the openWebNet==1.2.8 from Pypi

on hassbian type:

pip3 install OpenWebNet==1.2.8


HOW TO USE

Configuring the hub

my_home:
  host: IP address of the gateway es. '123.123.0.1'
  
  port: by default gateway use 20000, but if you use a different one write here
  
  password: if your gateway use a password, otherways include the IP address of your homeassistant server in the list of                  authorized IP

Configuring Light

light:
  - platform: my_home
    scan_interval: I suggest 5, every 5sec there is an update
    devices:
      - name: A name for your light
        indirizzo: the address on the bus for your light, is the value you set with 2 jumper on the  rele or wall switch es 72, 42 .....
        
        
Configuring thermal probe and/or central unit

sensor:
  - platform: my_home
    devices:
      - name: A name for your probe or central unit
        indirizzo: the address on the bus for your probe or central unit, is the value you set with 2 jumper on the  probe or central unit wall  es 11, 12 .....
        
Configuring switch

switch:
  - platform: my_home
    devices:
      - name: A name for your switch
        indirizzo: the address on the bus for your switch, is the value you set with 2 jumper on the  rele or wall switch es 72, 42 .....
  


