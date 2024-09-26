#!/usr/bin/python3
import rospy
import random
from geometry_msgs.msg import Point


rospy.init_node('publisher_1')

pub = rospy.Publisher('/comm', Point, queue_size=10)

while not rospy.is_shutdown():
    p = Point()
    p.x = 2
    p.y = 3
    p.z = 4

    pub.publish(p)
