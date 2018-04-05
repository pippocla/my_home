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
#REQUIREMENTS = ['OpenWebNet==1.0.1']
from OpenWebNet import OpenWebNet


PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    #vol.Required(CONF_HOST): cv.string,
    #vol.Required(CONF_PASSWORD): cv.string,
    #vol.Optional(CONF_PORT, default = '20000'): cv.string,
    vol.Required(CONF_DEVICES): vol.All(cv.ensure_list,[
        {
            vol.Required(CONF_NAME): cv.string,
            vol.Required('indirizzo'): cv.string,
        }
    ])
})



def setup_platform(hass, config, add_devices, discovery_info=None):
    """Setup the My Home Platform TEST"""

    #import OpenWebNet
    gate_data = hass.data[DOMAIN]
    print('gate',gate_data)
    gate=OpenWebNet(gate_data[0],gate_data[1],gate_data[2])
    add_devices(MyHomeLight(light,gate) for light in config[CONF_DEVICES])

class MyHomeLight(Light):
    """ Rappresentazione di una luce My Home """
    #import OpenWebNet

    def __init__ (self,light,gate):
        """Inizializzo MyHome light"""

        self._gate = gate
        self._name = light[CONF_NAME]
        self._indirizzo = light['indirizzo']
        self._state = False

    #@asyncio.coroutine
    #def async_added_to_hass(self):
    #    def _init_gate():
    #        self.get_status()
    #    yield from self.hass.async_add_job(_init_gate)

    @property
    def name(self):
        """Return the display name of this light """
        #import OpenWebNet

        return self._name

    #@property
    #def should_poll(self):
    #    return False


    @property
    def is_on(self):
        """Return true if the light is on """
        #import OpenWebNet

        return self._state

    def turn_on(self, **kwargs):
        """Instruct the light to turn on"""
        #import OpenWebNet
        print('luce on')
        self._gate.luce_on(self._indirizzo)

    def turn_off(self, **kwargs):
        """Instruct the light to turn off"""
        #import OpenWebNet
        print('luce off')
        self._gate.luce_off(self._indirizzo)

    def update(self):
        #import OpenWebNet
        print ('stato luce a indirizzo',self._indirizzo)
        self._state=self._gate.stato_luce(self._indirizzo)

    #def get_status(self):
    #    print ('stato luce a indirizzo',self._indirizzo)
    #    self._state=self._gate.stato_luce(self._indirizzo)
    #    self.schedule_update_ha_state()
