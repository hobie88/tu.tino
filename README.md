# tu.tino
Qbo distro based on Ubuntu 14.04 + ROS Indigo

This distro has been implemented by merging two Qbo repositories:
- Elpimous' Neorobot:  https://github.com/elpimous/Neo_robot/tree/master/INDIGO
- Manon's HumanRobotics: https://github.com/HumaRobotics/ros-indigo-qbo-packages 

If boards are not recognized:
check USB port in all  .yaml files, for each node
example:
port1: /dev/ttyUSB0 
port2: /dev/ttyUSB12
dmxPort: /dev/ttyUSB1
(for instance try switching USB1 and USB2)
