#!/usr/bin/python
# -*- coding: utf-8 -*-

# This file is part of easyNav-sensors-wifi.
# https://github.com/easyNav/easyNav-sensors-wifi

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2014 Joel Tong me@joeltong.org

from preggy import expect
import time

from easyNav_sensors_wifi import __version__
from easyNav_sensors_wifi import SensorWifi
from easyNav_sensors_wifi import SensorWifiDaemon
from tests.base import TestCase


class sensorWifiDaemonTestCase(TestCase):
    def test_can_get_wifi_data(self):

        d = SensorWifiDaemon()
        d.start()
        time.sleep(3)
        d.stop()

