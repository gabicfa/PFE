#! /usr/bin/env python

import rospy
from nav_msgs.msg import Odometry

position = []

def callback(msg):
    p = [msg.pose.pose.position.x, msg.pose.pose.position.y, msg.pose.pose.position.z]
    position.append(p)

rospy.init_node('check_odometry')
odom_sub = rospy.Subscriber('/bebop/odom', Odometry, callback)
rospy.spin()

print(position)
