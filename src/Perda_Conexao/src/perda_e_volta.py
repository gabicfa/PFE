#!/usr/bin/env python
# -*- coding: utf-8 -*-

import roslib; roslib.load_manifest('teleop_twist_keyboard')
import rospy

from geometry_msgs.msg import Twist, Vector3
from nav_msgs.msg import Odometry
from std_msgs.msg import Empty, String

import sys, select, termios, tty

import numpy as np
import math

pub = rospy.Publisher('bebop/cmd_vel', Twist, queue_size = 1)
pub2 = rospy.Publisher('bebop/takeoff', Empty, queue_size = 1)
pub3 = rospy.Publisher('bebop/land', Empty, queue_size = 1)
empty_msg = Empty()

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

teleop = []
# global p = []

def getKey():
        tty.setraw(sys.stdin.fileno())
        select.select([sys.stdin], [], [], 0)
        key = sys.stdin.read(1)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
        return key

def vels(speed,turn):
        return "currently:\tspeed %s\tturn %s " % (speed,turn)

def veloc(vel):
	global pub
	pub.publish(vel)

def callback(msg):
    x = "%.5f" % msg.pose.pose.position.x
    y = "%.5f" % msg.pose.pose.position.y
    z = "%.5f" % msg.pose.pose.position.z
    global p 
    p = [x, y, z]
#     print(p)
    if(len(teleop)==0):
        teleop.append(p)
    elif(p != teleop[len(teleop)-1]):
        teleop.append(p)

def caminho_de_volta(tel):
        #Caminho a partir de distância mínima entre pontos
        teleop = np.asarray(tel, dtype=np.float32)

        Pos_atual = teleop[-1]

        Home = teleop[0]

        delta_seguro = 1 # distância entre pontos considerada segura        

        caminho = np.array([Pos_atual])
        t = 0

        # Caminho ótimo
        # while not distancia(Pos_atual, [0,0,0], 0.1):
        while not np.array_equal(Pos_atual,Home): 
                t+= 1
                if t > 10000:
                        break
                #A cada posição atual, faz-se uma busca dos pontos dentro do raio de distância de segurança
                #Os parâmetros abaixo são "resetados" a cada busca
                primeiro_valor = 0 #será o ponto mais "cedo" entre os pontos dentro do raio de segurança (ele só será usado caso não seja mais possível se deslocar em direção ao home)
                apagar_valores = False 
                dist_home = 0 #distância de um ponto dentro do raio de segurança até o home
                dist_prox_home = 0 # menor distância entre um dos pontos dentro do raio de segurança até o home   
                pontos_seguros = [] #índices dos pontos que estão dentro do raio de segurança


                for i in range (0,len(teleop)):
                        #Para cada pondo, partindo da origem, testar se está dentro do raio de segurança
                        dist = math.sqrt((teleop[i,0] - Pos_atual[0])**2 + (teleop[i,1] - Pos_atual[1])**2 + (teleop[i,2] - Pos_atual[2])**2)
                        
                        if dist <= delta_seguro and primeiro_valor == 0: #primeiro valor dentro do raio de segurança
                                menor_index = teleop[i]
                                pontos_seguros.append(i)
                                dist_prox_home = math.sqrt((teleop[i,0] - Home[0])**2 + (teleop[i,1] - Home[1])**2 + (teleop[i,2] - Home[2])**2)
                                prox = teleop[i]
                                primeiro_valor = 1 
                        
                        
                        elif dist <= delta_seguro and primeiro_valor == 1: #confere se o novo valor dentro do raio é mais perto ou não do home
                                pontos_seguros.append(i)
                                dist_home = math.sqrt((teleop[i,0] - Home[0])**2 + (teleop[i,1] - Home[1])**2 + (teleop[i,2] - Home[2])**2)
                                
                                if  dist_home < dist_prox_home:
                                        dist_prox_home = dist_home
                                        prox = teleop[i]

                # if distancia(prox,Pos_atual, 0.1): #caso nenhum ponto seja mais proximo do home do que aquele que já está, vai ter que andar para trás
                if np.array_equal(prox,Pos_atual): #caso nenhum ponto seja mais proximo do home do que aquele que já está, vai ter que andar para trás
                        # prox = menor_index
                        apagar_valores = True
                        
                caminho = np.vstack([caminho,prox])
                Pos_atual = caminho[-1]

                if apagar_valores == True:
                        for r in pontos_seguros:
                                teleop[r] = Home
        return caminho

def volta(caminho):
        caminho.tolist()
        land = False
        while not land:
                for i in range(1, len(caminho)):
                        print("Ponto: " + str(i))
                        delta_x = float(caminho[i][0]) - float(p[0])
                        delta_y = float(caminho[i][1]) - float(p[1])
                        delta_z = float(caminho[i][2]) - float(p[2])
                        print(delta_x)
                        print(delta_y)
                        print(delta_z)

                        while(abs(delta_x)>0.1 or abs(delta_y)>0.1 or abs(delta_z)>0.1):
                                print("Posicao q estou: " + str(p[0]) + ", " + str(p[1]) + ", " + str(p[2]))
                                print("Velocidadede: " + str(delta_x) + ", " + str(delta_y) + ", " + str(delta_z))
                                print("Posicao q quero ir: " + str(caminho[i][0]) + ", " + str(caminho[i][1]) + ", " + str(caminho[i][2]))
                                print ('\n')
                                x_angular = 0
                                y_angular = 0
                                z_angular = 0 
                                vel = Twist(Vector3(-delta_y, delta_x, delta_z), Vector3(x_angular, y_angular, z_angular))
                                veloc(vel)
                                rospy.sleep(1)
                                if(abs(delta_x)>0.1):
                                        delta_x = float(caminho[i][0]) - float(p[0])
                                
                                if(abs(delta_y)>0.1):
                                        delta_y = float(caminho[i][1]) - float(p[1])
                                
                                if(abs(delta_z)>0.1):
                                        delta_z = float(caminho[i][2]) - float(p[2])
                                
                                
                        
                                
                land = True
        pub3.publish(empty_msg)


if __name__=="__main__":

    settings = termios.tcgetattr(sys.stdin)
    rospy.init_node('check_odometry')
    speed = rospy.get_param("~/speed", 0.5)
    turn = rospy.get_param("~/turn", 1.0)
    odom_sub = rospy.Subscriber('/bebop/odom', Odometry, callback)
    
    x = 0
    y = 0
    z = 0
    th = 0
    status = 0
    connection = True

    try:
        print (msg)
        print (vels(speed,turn))
        while(connection):
                key = getKey()
                if key in moveBindings.keys():
                        x = moveBindings[key][0]
                        y = moveBindings[key][1]
                        z = moveBindings[key][2]
                        th = moveBindings[key][3]
                elif key in speedBindings.keys():
                        speed = speed * speedBindings[key][0]
                        turn = turn * speedBindings[key][1]

                        print (vels(speed,turn))
                        if (status == 14):
                                print (msg)
                        status = (status + 1) % 15
                elif key == '1':
                        pub2.publish(empty_msg)
                elif key == '2':
                        pub3.publish(empty_msg)
                elif key =='a':
                        connection = False
                        print("Perda de Conexao")
                        print("teleop")
                        for t in teleop:
                            print(t)
                        print("caminho")
                        caminho = caminho_de_volta (teleop)
                        print(caminho)
                        volta(caminho)
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
            print ("erro")

    finally:
            twist = Twist()
            twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
            twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
            pub.publish(twist)

            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
