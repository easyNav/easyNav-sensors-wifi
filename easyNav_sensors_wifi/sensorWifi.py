#!/usr/bin/python
# -*- coding: utf-8 -*-

# This file is part of easyNav-sensors-wifi.
# https://github.com/easyNav/easyNav-sensors-wifi

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2014 Joel Tong me@joeltong.org

import logging
import subprocess
import re




class SensorWifi:
    def __init__(self, interface='wlan0'):
        """ Creates new SensorWifi instance, scanning the specified interface. 
        """
        self.interface = interface
        pass


    def get(self):
        """ Returns the iwlist data, as a dictionary
        """
        class line_matcher:
            def __init__(self, regexp, handler):
                self.regexp  = re.compile(regexp)
                self.handler = handler

        def handle_new_network(line, result, networks):
            # group(1) is the mac address
            networks.append({})
            ## TODO: this is fix to delete LSB 2 bytes.  Move to option later to get full 32 bytes.
            networks[-1]['Address'] = result.group(1)[:-3]

        def handle_essid(line, result, networks):
            # group(1) is the essid name
            networks[-1]['ESSID'] = result.group(1)

        def handle_quality(line, result, networks):
            # group(1) is the quality value
            # group(2) is probably always 100
            ## TODO : The below will return strength / 70
            # networks[-1]['Quality'] = result.group(1) + '/' + result.group(2)
            ## TODO: Move this to option.  This is fix for easyNAv specific purposes only.
            networks[-1]['Quality'] = int(result.group(1))

        def handle_unknown(line, result, networks):
            # group(1) is the key, group(2) is the rest of the line
            networks[-1][result.group(1)] = result.group(2)

        ## Do actual stuff here #####################################

        proc = subprocess.Popen(['sudo', '/sbin/iwlist', self.interface, 'scan'],
                                stdout=subprocess.PIPE)
        stdout, stderr =  proc.communicate()

        lines = stdout.split('\n')

        networks = []
        matchers = []

        # catch the line 'Cell ## - Address: XX:YY:ZZ:AA:BB:CC'
        matchers.append(line_matcher(r'\s+Cell \d+ - Address: (\S+)',
                                     handle_new_network))
        
        # catch the line 'ESSID:"network name"
        matchers.append(line_matcher(r'\s+ESSID:"([^"]+)"', 
                                     handle_essid))

        # catch the line 'Quality:X/Y Signal level:X dBm Noise level:Y dBm'
        matchers.append(line_matcher(r'\s+Quality=(\d+)/(\d+)',
                                     handle_quality))

        # catch any other line that looks like this:
        # Key:value
        matchers.append(line_matcher(r'\s+([^:]+):(.+)',
                                     handle_unknown))

        # read each line of output, testing against the matches above
        # in that order (so that the key:value matcher will be tried last)
        for line in lines:
            for m in matchers:
                result = m.regexp.match(line)
                if result:
                    m.handler(line, result, networks)
                    break

        return networks

        # for n in networks:
        #     print 'Found network', n['Address'], n['ESSID'], 'Quality', n.get('Quality')
        #     # to see the whole dictionary:
        #     # print n
            
        # print "NUMBER OF NETWORKS: %s" % len(networks)
