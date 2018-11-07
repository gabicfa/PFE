#!/usr/bin/env python
import roslib; roslib.load_manifest('teleop_twist_keyboard')
import rospy

from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from std_msgs.msg import Empty

import sys, select, termios, tty

msg = """
Reading from the keyboard  and Publishing to Twist!
---------------------------
Moving around:
   u    i    o
   j    k    l
   m    ,    .

For Holonomic mode (strafing), hold down the shift key:
---------------------------
   U    I    O
   J    K    L
   M    <    >

t : up (+z)
b : down (-z)

anything else : stop

q/z : increase/decrease max speeds by 10%
w/x : increase/decrease only linear speed by 10%
e/c : increase/decrease only angular speed by 10%

CTRL-C to quit
"""

moveBindings = {
                'i':(1,0,0,0),
                'o':(1,0,0,-1),
                'j':(0,0,0,1),
                'l':(0,0,0,-1),
                'u':(1,0,0,1),
                ',':(-1,0,0,0),
                '.':(-1,0,0,1),
                'm':(-1,0,0,-1),
                'O':(1,-1,0,0),
                'I':(1,0,0,0),
                'J':(0,1,0,0),
                'L':(0,-1,0,0),
                'U':(1,1,0,0),
                '<':(-1,0,0,0),
                '>':(-1,-1,0,0),
                'M':(-1,1,0,0),
                't':(0,0,1,0),
                'b':(0,0,-1,0),
               }

speedBindings={
                'q':(1.1,1.1),
                'z':(.9,.9),
                'w':(1.1,1),
                'x':(.9,1),
                'e':(1,1.1),
                'c':(1,.9),
              }
position = []

def getKey():
        tty.setraw(sys.stdin.fileno())
        select.select([sys.stdin], [], [], 0)
        key = sys.stdin.read(1)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
        return key


def vels(speed,turn):
        return "currently:\tspeed %s\tturn %s " % (speed,turn)

def callback(msg):
    x = "%.5f" % msg.pose.pose.position.x
    y = "%.5f" % msg.pose.pose.position.y
    z = "%.5f" % msg.pose.pose.position.z
    p = [x, y, z]
    if(len(position)==0):
        position.append(p)
    elif(p != position[len(position)-1]):
        position.append(p)

if __name__=="__main__":
        settings = termios.tcgetattr(sys.stdin)
        
	pub = rospy.Publisher('bebop/cmd_vel', Twist, queue_size = 1)
        rospy.init_node('check_odometry')
	pub2 = rospy.Publisher('bebop/takeoff', Empty, queue_size = 1)
	pub3 = rospy.Publisher('bebop/land', Empty, queue_size = 1)
	empty_msg = Empty()

        speed = rospy.get_param("~/speed", 0.5)
        turn = rospy.get_param("~/turn", 1.0)
        
        x = 0
        y = 0
        z = 0
        th = 0
        status = 0
        connection = True

        try:
                print msg
                print vels(speed,turn)
                while(connection):
                        odom_sub = rospy.Subscriber('/bebop/odom', Odometry, callback)
                        key = getKey()
                        if key in moveBindings.keys():
                                x = moveBindings[key][0]
                                y = moveBindings[key][1]
                                z = moveBindings[key][2]
                                th = moveBindings[key][3]
                        elif key in speedBindings.keys():
                                speed = speed * speedBindings[key][0]
                                turn = turn * speedBindings[key][1]

                                print vels(speed,turn)
                                if (status == 14):
                                        print msg
                                status = (status + 1) % 15
                        elif key == '1':
                                pub2.publish(empty_msg)
                        elif key == '2':
                                pub3.publish(empty_msg)
                        elif key =='a':
                                connection = False
                                print("Perda de Conexao")
                                for l in position:
                                        print(l)
                        else:
                                x = 0
                                y = 0
                                z = 0
                                th = 0
                                if (key == '\x03'):
                                        break

                        twist = Twist()
                        twist.linear.x = x*speed; twist.linear.y = y*speed; twist.linear.z = z*speed
                        twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = th*turn
                        pub.publish(twist)
                        

        except:
                print e

        finally:
                twist = Twist()
                twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
                twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
                pub.publish(twist)

                termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
