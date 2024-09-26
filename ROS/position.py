#!/usr/bin/python3

import rospy
from geometry_msgs.msg import Point
import random
from std_msgs.msg import Float64

rospy.init_node('posicao')

pub = rospy.Publisher('posicao', Float64, queue_size=10)

while not rospy.is_shutdown():
    p = random.randint(0,100000)
    pub.publish(p)

