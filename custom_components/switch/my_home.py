#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Support for My Home Platform TEST light71

"""
import logging
import voluptuous as vol
import asyncio

from homeassistant.components.switch import SwitchDevice, PLATFORM_SCHEMA
from homeassistant.const import CONF_HOST, CONF_PASSWORD, CONF_PORT, CONF_NAME, CONF_DEVICES
from custom_components.my_home import DOMAIN
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
    add_devices(MyHomeSwitch(switch,gate) for switch in config[CONF_DEVICES])

class MyHomeSwitch(SwitchDevice):
    """ Rappresentazione di uno switch My Home """


    def __init__ (self,switch,gate):
        """Inizializzo MyHome switchDevice"""

        self._gate = gate
        self._name = switch[CONF_NAME]
        self._indirizzo = switch['indirizzo']
        self._state = False

    @asyncio.coroutine
    def async_added_toHass(self):
        #self.get_status()
        yield from self.hass.async_add_job(update())


    @property
    def name(self):
        """Return the display name of this light """


        return self._name



    @property
    def is_on(self):
        """Return true if the switch is on """
        #import OpenWebNet

        return self._state

    def turn_on(self, **kwargs):
        """Instruct the switch to turn on"""
        #import OpenWebNet

        self._gate.luce_on(self._indirizzo)

    def turn_off(self, **kwargs):
        """Instruct the switch to turn off"""
        #import OpenWebNet

        self._gate.luce_off(self._indirizzo)

    def get_status(self):
        #import OpenWebNet
        #print('get_status light')
        self._gate.ask_stato_luce(self._indirizzo)
        self._state=self._gate.answ_stato_luce(self._indirizzo)

        self.schedule_update_ha_state()
