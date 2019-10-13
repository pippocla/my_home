#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Support for My Home Platform TEST Temp Sensor

"""
import logging
import voluptuous as vol
import asyncio
import time


from homeassistant.components.sensor import PLATFORM_SCHEMA

from homeassistant.const import CONF_TYPE,TEMP_CELSIUS, CONF_HOST, CONF_PASSWORD, CONF_PORT, CONF_NAME, CONF_DEVICES
from custom_components.my_home import DOMAIN
from homeassistant.helpers.entity import Entity
import homeassistant.helpers.config_validation as cv


_LOGGER = logging.getLogger(__name__)

DOMAIN = "my_home"
DEPENDENCIES = ['my_home']

from OpenWeb import OpenWeb

SENSOR_TYPES = {
    "Temperature": ["Temperature", TEMP_CELSIUS, "", None],
    "SetTemperature": ["SetTemperature", TEMP_CELSIUS, "", None],
    "Valve_State": ["Valve_State", "", "mdi:play-network-outline", None],
    "Gateway_Time": ["Gateway_Time","","mdi:clock-outline", None],
    "Gateway_IP": ["Gateway_IP", "", "mdi:home-automation", None],
    "Gateway_Model": ["Gateway_Model", "", "mdi:home-circle", None],
    "Gateway_Firmware": ["Gateway_Firmware", "", "mdi:home-import-outline", None],
    "Gateway_Uptime": ["Gateway_Uptime", "", "mdi:home-analytics", None],

}

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({

    vol.Required(CONF_DEVICES): vol.All(cv.ensure_list,[
        {
            vol.Required(CONF_TYPE): vol.In(SENSOR_TYPES),
            vol.Required('Name'): cv.string,
            vol.Required('indirizzo'): cv.string,
        }
    ])
})



def setup_platform(hass, config, add_devices, discovery_info=None):
    """Setup the My Home Platform TEST"""



    gate = hass.data[DOMAIN]

    add_devices(MyHomeTempSensor(sensor,gate) for sensor in config[CONF_DEVICES])

class MyHomeTempSensor(Entity):
    """ Rappresentazione di un Sensore di Temperatura My Home """
    #import OpenWebNet

    def __init__ (self,sensor_type,gate):
        """Inizializzo MyHome light"""

        self._gate = gate
        self.type = sensor_type['type']
        self._name = sensor_type['Name']
        self._indirizzo = sensor_type['indirizzo']
        self._unit_of_measurement = SENSOR_TYPES.get(sensor_type['type'])[1]
        self._state = False
        print('sensortype',self.type)
        print('name',self._name)


    @property
    def name(self):

        """Return the display name of this light """
        return self._name

    @property
    def device_clas(self):

        """Retunr the class of this sensor."""
        return SENSOR_TYPES.get(self.type)[3]

    @property
    def icon(self):

        """Icon to use in the frontend, if any."""
        return SENSOR_TYPES.get(self.type)[2]


    @property
    def state(self):

        """Return state of the sensor """
        return self._state

    @property
    def unit_of_measurement(self):
        """Return the measure unit """
        return self._unit_of_measurement

    def update(self):

        print('update sensor type',self.type)
        print('update sensor name',self._name)
        if self.type == 'SetTemperature':
            self._gate.cmd_open("4",'14',self._indirizzo)
            self._state = self._gate.setTemperature_status(self._indirizzo)
        elif self.type == 'Temperature':
            self._gate.cmd_open("4",'0',self._indirizzo)
            self._state = self._gate.temperature_status(self._indirizzo)
        elif self.type == 'Valve_State':
            self._gate.cmd_open('4','19',self._indirizzo)
            self._state = self._gate.valveState_status(self._indirizzo)
        elif self.type == 'Gateway_Time':
            print('Gateway Time request from hass')
            self._gate.cmd_open('13','0','')
            self._state = self._gate.gateway_Status('0')
        elif self.type == 'Gateway_IP':
            print('Gateway IP request from hass')
            self._gate.cmd_open('13','10','')
            self._state = self._gate.gateway_Status('10')
        elif self.type == 'Gateway_Model':
            print('Gateway Model request from hass')
            self._gate.cmd_open('13','15','')
            self._state = self._gate.gateway_Status('15')
        elif self.type == 'Gateway_Firmware':
            print('Gateway Firmware request from hass')
            self._gate.cmd_open('13','16','')
            self._state = self._gate.gateway_Status('16')
        elif self.type == 'Gateway_Uptime':
            print('Gateway Uptime request from hass')
            self._gate.cmd_open('13','19','')
            self._state = self._gate.gateway_Status('19')
