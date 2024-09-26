#!/usr/bin/python3

import rospy

from std_msgs.msg import Float32
from geometry_msgs.msg import Point

rospy.init_node('sub')

repub = rospy.Publisher('repub',Float32, queue_size=10)

def callback(data):
    n = data.x*data.x + data.y*data.y + data.z*data.z 
    repub.publish(n)

while not rospy.is_shutdown():
    rospy.Subscriber('comm', Point, callback)
    rospy.spin()
