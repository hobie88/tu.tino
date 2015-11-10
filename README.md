# tu.tino
Qbo distro based on Ubuntu 11.10 (Oneiric Ocelot) + ROS Electric

This distro has been implemented starting from Qbo official Distro:
- http://www.openqbo.org/downloads/openqbo_beta04.1-64bits.iso

If boards are not recognized: check USB port in all  .yaml files, for each node 
example:

port1: /dev/ttyUSB0

port2: /dev/ttyUSB12

dmxPort: /dev/ttyUSB1

(for instance try switching USB1 and USB2)
 
