#!/usr/bin/python3

import rospy
from std_msgs.msg import Float64
from geometry_msgs.msg import Point

posicao_atual = 0.0
velocidade_atual = 0.0

def sensor_posicao(data):
    global posicao_atual
    posicao_atual = data.data

def sensor_velocidade(data):
    global velocidade_atual
    velocidade_atual = data.data

def controlador():
    rospy.init_node('controller')

    rospy.Subscriber('posicao', Float64, sensor_posicao)
    rospy.Subscriber('velocidade', Float64, sensor_velocidade)
    
    pub = rospy.Publisher('posicao_prevista', Float64, queue_size=10)
    rate = rospy.Rate(10)

    dt = 1/10

    while not rospy.is_shutdown():
        
        posicao_prevista = posicao_atual + velocidade_atual*dt
        pub.publish(posicao_prevista)
        rate.sleep()

if __name__ == '__main__':
    try:
        controlador()
    except rospy.ROSInterruptException:
        pass
