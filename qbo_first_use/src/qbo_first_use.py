#!/usr/bin/env python
# coding: utf-8
#
# Software License Agreement (GPLv2 License)
#
# Copyright (c) 2011 Thecorpora, S.L.
#
# This program is free software; you can redistribute it and/or 
# modify it under the terms of the GNU General Public License as 
# published by the Free Software Foundation; either version 2 of
# the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License 
# along with this program; if not, write to the Free Software 
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, 
# MA 02110-1301, USA.
#
# Authors: Arturo Bajuelos <arturo@openqbo.com>

import roslib; roslib.load_manifest('qbo_first_use')
import rospy

from qbo_talk.srv import Text2Speach

#ROS Publishers
global client_speak


def speak_this(text):
    global client_speak
    client_speak(str(text))


def main():
    global client_speak
    rospy.init_node("qbo_first_use")
    rospy.loginfo("Launching Qbo First Use")


    file_path=roslib.packages.get_pkg_dir('qbo_first_use')+"/FIRST_FILE"

    file_exists = True
    try:
       with open(file_path) as f: pass
    except IOError as e:
       file_exists = False

    if file_exists:
       rospy.loginfo("Qbo First Use program has terminated because this isn't Qbo first use")
       return
    else:
       rospy.loginfo("Launching Qbo First use procedure")


    client_speak = rospy.ServiceProxy("/qbo_talk/festival_say_no_wait", Text2Speach)
    rospy.wait_for_service('/qbo_talk/festival_say_no_wait')
    
    speak_this("This is my first boot... Please connect me to a local network by following the instructions on the manual")
    open(file_path, 'w').close()

if __name__ == '__main__':
    main()


