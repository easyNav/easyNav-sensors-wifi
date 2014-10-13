#!/usr/bin/python
# -*- coding: utf-8 -*-

# This file is part of easyNav-sensors-wifi.
# https://github.com/easyNav/easyNav-sensors-wifi

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2014 Joel Tong me@joeltong.org



import logging
import time
import threading

import smokesignal

from sensorWifi import SensorWifi



class SensorWifiDaemon:

    def __init__(self, args=None):
        self._sw = SensorWifi('wlan0')
        pass


    def start(self):
        """Starts running the thread 
        """
        self._active = True

        ## Run tick thread
        def runThread():
            while(self._active):
                self._tick()
                time.sleep(0.2)

        self._threadListen = threading.Thread(target=runThread)
        self._threadListen.start()
        print 'Wifi Sniffer Daemon: Thread started.'


    def stop(self):
        """ Stops running the thread
        """
        self._active = False
        self._threadListen.join()
        logging.info('Wifi Sniffer Daemon: Thread stopped.')


    def _tick(self):
        """Tick function executed in daemon
        """
        networks = self._sw.get()
        smokesignal.emit('onNetworkData', networks)


    def getStength(self):
        result = None 
        return result




###################################
##  Main program defined here    ##
###################################

def runMain():
    """ Main function called when run as standalone daemon
    """

    def configLogging():
        logging.getLogger('').handlers = []

        logging.basicConfig(
            # filename = "a.log",
            # filemode="w",
            level = logging.DEBUG)

        configLogging()
    daemon = SensorWifiDaemon()
    print 'Welcome to Wifi Daemon.'
    print 'Sniffing networks..'
    daemon.start()


if __name__ == '__main__':
    runMain()



