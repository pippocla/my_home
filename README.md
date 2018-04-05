# Beta test for implement My Home bTicino platform in Home Assistant

Create under configuration directory a new directory custom_components,
then copy the file in the same directory they are here.

Merge configurator.yaml with your file.

How to use 

configuring the hub

my_home:
  host: IP address of the gateway es. 123.123.0.1
  port: by default gateway use 20000, but if you use a different one write here
  password: if your gateway use a password, otherways include the IP address of your homeassistant server in the list of                  authorized IP

configuring Light

light:
  - platform: my_home
    devices:
      - name: A name for your light
        indirizzo: the address on the bus for your light, is the value you set with 2 jumper on the  rele or wall switch es 72, 42 .....
        
        
configuring thermal probe and/or central unit

sensor:
  - platform: my_home
    devices:
      - name: A name for your probe or central unit
        indirizzo: the address on the bus for your probe or central unit, is the value you set with 2 jumper on the  probe or central unit wall  es 11, 12 .....
