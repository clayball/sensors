#!/usr/bin/env python

# Clay Wells
#
# Create a sensor to listen for UDP packets sent to reserved port 0.
#
# An iptables rule is used to redirect 0/UDP packets to 30999/UDP. Only a process executed
# as root can listen on ports 0-1024.
#
# Listen on port 30999/UDP (so an unprivileged user can run this)
# Write data received to a file for processing later. 
# - include timestamp

import sys
from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
from datetime import datetime

# Open the output file in append mode
ofile = open('udp-received.log', 'a')

class Echo(DatagramProtocol):

    def datagramReceived(self, data, (host, port)):
    	# get time stamp
    	now = datetime.now()
        ofile.write('received %r from %s:%d at %s\n' % (data, host, port, now))
        self.transport.write(data, (host, port))

reactor.listenUDP(30999, Echo())
reactor.run()
