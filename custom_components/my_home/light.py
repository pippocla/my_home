#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Support for My Home Platform TEST light71

"""
import logging
import voluptuous as vol
import asyncio

from homeassistant.components.light import Light, PLATFORM_SCHEMA
from homeassistant.const import CONF_HOST, CONF_PASSWORD, CONF_PORT, CONF_NAME, CONF_DEVICES
from custom_components.my_home import DOMAIN
import homeassistant.helpers.config_validation as cv


_LOGGER = logging.getLogger(__name__)

DOMAIN = "my_home"
DEPENDENCIES = ['my_home']

from OpenWeb import OpenWeb


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


    #gate_data = hass.data[DOMAIN]
    gate = hass.data[DOMAIN]
    print('gate',gate)
    #gate=OpenWebNet(gate_data[0],gate_data[1],gate_data[2])
    add_devices(MyHomeLight(light,gate) for light in config[CONF_DEVICES])

class MyHomeLight(Light):
    """ Rappresentazione di una luce My Home """


    def __init__ (self,light,gate):
        """Inizializzo MyHome light"""

        self._gate = gate
        self._name = light[CONF_NAME]
        self._indirizzo = light['indirizzo']
        self._state = False
        self._first = {}



    @property
    def name(self):
        """Return the display name of this light """


        return self._name



    @property
    def is_on(self):
        """Return true if the light is on """

        return self._state

    def turn_on(self, **kwargs):
        """Instruct the light to turn on"""

        self._gate.cmd_open("1","1",self._indirizzo)


    def turn_off(self, **kwargs):
        """Instruct the light to turn off"""

        self._gate.cmd_open("1","0",self._indirizzo)


    def update(self):

        if not self._first.get(self._indirizzo) :

            self._first[self._indirizzo]='1'
            print('self_first update',self._first)
            self._gate.cmd_open("1",'',self._indirizzo)
        self._state = self._gate.light_status(self._indirizzo)
