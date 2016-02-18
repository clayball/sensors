Sensors
=======

One of our darknet sensors receives over one hundred probes on port 0/UDP. To better understand what this traffic is and where it's coming from, I decided to add a sensor to see if I can find out more information. This is the approach I took. Minor tweaks will likely be necessary.

I need a sensor that listens to UDP requests on port 0. So, what is port 0 all about anyway? The first placed I looked is /etc/services which references IANA for all port assignments. Port 0 is not listed in /etc/services. This is because port 0 TCP/UDP is reserved.

A quick break down on port assigns:

- The Well Known Ports are those from 0 through 1023.
- The Registered Ports are those from 1024 through 49151
- The Dynamic and/or Private Ports are those from 49152 through 65535

The latest IANA port assignments can be found on IANA's website,

http://www.iana.org/assignments/port-numbers

IANA references RFC 6335, https://tools.ietf.org/html/rfc6335

## Setup ##

Redirect UDP packets arriving at port 0 to port 30999. I'm just picking an arbitrary high port number.

iptables -t nat -A PREROUTING -p udp --dport 0 -j REDIRECT --to-port 30999

Start sensor-udp.py and watch the log file.


` # ./sensor-udp.py &`

` # tail -f udp-received.log`

## Testing the sensor ##

The sensor will run on host 192.168.1.13. The test will be run from a different host on the same subnet.

`nping --udp 192.168.1.13 -p 30999`

