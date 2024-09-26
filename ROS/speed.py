#!/usr/bin/python3

import rospy
from geometry_msgs.msg import Point
import random
from std_msgs.msg import Float64

rospy.init_node('velocidade')
pub = rospy.Publisher('velocidade', Float64, queue_size=10)
while not rospy.is_shutdown():
    p = random.randint(0,100)
    pub.publish(p)
