#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Support for My Home Platform TEST Temp Sensor

"""
import logging
import voluptuous as vol
import asyncio


from homeassistant.components.sensor import PLATFORM_SCHEMA

from homeassistant.const import TEMP_CELSIUS, CONF_HOST, CONF_PASSWORD, CONF_PORT, CONF_NAME, CONF_DEVICES
from custom_components.my_home import DOMAIN
from homeassistant.helpers.entity import Entity
import homeassistant.helpers.config_validation as cv


_LOGGER = logging.getLogger(__name__)

DOMAIN = "my_home"
DEPENDENCIES = ['my_home']

from OpenWebNet import OpenWebNet


PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({

    vol.Required(CONF_DEVICES): vol.All(cv.ensure_list,[
        {
            vol.Required(CONF_NAME): cv.string,
            vol.Required('indirizzo'): cv.string,
        }
    ])
})



def setup_platform(hass, config, add_devices, discovery_info=None):
    """Setup the My Home Platform TEST"""



    gate = hass.data[DOMAIN]
    #gate_data = hass.data[DOMAIN]
    #gate=OpenWebNet(gate_data[0],gate_data[1],gate_data[2])
    add_devices(MyHomeTempSensor(sensor,gate) for sensor in config[CONF_DEVICES])

class MyHomeTempSensor(Entity):
    """ Rappresentazione di un Sensore di Temperatura My Home """
    #import OpenWebNet

    def __init__ (self,sensor,gate):
        """Inizializzo MyHome light"""

        self._gate = gate
        self._name = sensor[CONF_NAME]
        self._indirizzo = sensor['indirizzo']
        self._state = False

    @asyncio.coroutine
    def async_added_toHass(self):
        self.get_status()
        yield from self.hass.async_add_job(update())

    @property
    def name(self):

        """Return the display name of this light """
        return self._name


    @property
    def state(self):

        """Return state of the sensor """
        return self._state

    @property
    def unit_of_measurement(self):
        """Return the measure unit """
        return TEMP_CELSIUS

    def update(self):
        #print('get temperature')


        if self._name[:3] == 'SET':
            self._gate.ask_read_setTemperature(self._indirizzo)
            self._state=self._gate.answ_read_setTemperature(self._indirizzo)
        else:
            self._gate.ask_read_temperature(self._indirizzo)
            self._state=self._gate.answ_read_temperature(self._indirizzo)
        self.schedule_update_ha_state()
