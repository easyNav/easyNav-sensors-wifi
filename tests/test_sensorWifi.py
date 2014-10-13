#!/usr/bin/python
# -*- coding: utf-8 -*-

# This file is part of easyNav-sensors-wifi.
# https://github.com/easyNav/easyNav-sensors-wifi

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2014 Joel Tong me@joeltong.org

from preggy import expect

from easyNav_sensors_wifi import __version__
from easyNav_sensors_wifi import SensorWifi
from tests.base import TestCase


class sensorWifiTestCase(TestCase):
    def test_can_get_wifi_data(self):
        sw = SensorWifi(interface='wlan0')
        networks = sw.get()
        expect(type(networks) is list).to_equal(True)

        for n in networks:
            expect(type(n) is dict).to_equal(True)

