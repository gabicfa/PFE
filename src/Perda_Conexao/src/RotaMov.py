#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 10:10:56 2018

@author: Bruna
"""
import numpy as np
import random
import rospy
import math
from std_msgs.msg import String
from std_msgs.msg import Empty
from geometry_msgs.msg import Twist, Vector3

def takeoff(): #Publica nas vari'aveis para realizar a funcao
	global pub_TakeOff
	pub_TakeOff.publish(Empty())


def land():
	global pub_land
	pub_Land.publish(Empty())

def veloc(vel):
	global pub_Vel
	pub_Vel.publish(vel)

# import matplotlib.pyplot as plt

# simular uma matriz da Gabi
teleop = np.array([[0,0,0]])

x = teleop[0,0]
y = teleop[0,1]
z = teleop[0,2]

for i in range (0,100): #tamanho da matriz trazida pela gabi
    movimento = random.choice(['x','y'])#no momento o movimento é só x e y
    sentido = random.choice(['+','-'])
    
    if movimento == 'x':
        if sentido == "+":
            x += 10
        elif sentido == '-':
            x -= 10
        
    elif movimento == 'y':
        if sentido == "+":
            y += 10
        elif sentido == '-':
            y -= 0
            
#    elif movimento == 'z':
#        if sentido == "+":
#            z += 10
#        elif sentido == '-':
#            z -= 10

    add = np.array([x,y,z])
    teleop = np.vstack([teleop,add])

teleop2 = [
['0.00000', '0.00000', '0.00000'],
['0.05407', '0.02661', '0.17428'],
['0.09026', '0.01151', '0.68701'],
['0.13697', '0.08482', '0.86850'],
['0.11243', '0.13735', '0.92222'],
['0.16584', '0.21857', '0.92815'],
['0.20624', '0.28535', '0.93429'],
['0.21782', '0.30349', '0.93668'],
['0.27897', '0.51787', '0.94756'],
['0.31485', '0.60339', '0.96150'],
['0.28923', '0.59780', '0.97751'],
['0.32953', '0.73743', '1.01614'],
['0.30144', '0.73642', '1.04326'],
['0.30902', '0.73612', '1.05880'],
['0.31094', '0.71286', '1.07102'],
['0.34452', '0.97391', '0.44883'],
['0.35287', '1.06632', '0.03868'],]

teleop = np.asarray(teleop2, dtype=np.float32)

#Caminho a partir de distância mínima entre pontos

Pos_atual = teleop[-1]

Home = teleop[0]


delta_seguro = 0.001 # distância entre pontos considerada segura        

caminho = np.array([Pos_atual])
t = 0# apenas uma variável para não deixar o while entrar em loop infinito
#teleoporg = teleop.copy()
#teleoporg.view('i8,i8,i8').sort(order=['f0', 'f1','f2'], axis=0)

print(teleop)
print('\n')
# Caminho ótimo
while not np.array_equal(Pos_atual,[0,0,0]):
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
    
    if np.array_equal(prox,Pos_atual): #caso nenhum ponto seja mais proximo do home do que aquele que já está, vai ter que andar para trás
        prox = menor_index
        apagar_valores = True
        
    caminho = np.vstack([caminho,prox])
    Pos_atual = caminho[-1]
    
    if apagar_valores == True:
        for r in pontos_seguros:
            teleop[r] = [0,0,0]
    

print(caminho)    

# if __name__ == '__main__':
# 	rospy.init_node('drone')
# 	pub_TakeOff = rospy.Publisher("bebop/takeoff", Empty, queue_size=10) #Define variaveis
# 	pub_Land = rospy.Publisher("bebop/land", Empty, queue_size=10)
# 	pub_Vel = rospy.Publisher("bebop/cmd_vel", Twist, queue_size=10)
# 	rate = rospy.Rate(10) # 10hz
# 	count = 0
# 	estado = 0
# 	while not rospy.is_shutdown():
# 		for i in caminho:
# 			x_linear = i[0]#
# 			y_linear = i[1]#
# 			z_linear = i[2]

# 			x_angular = 0
# 			y_angular = 0
# 			z_angular = 0 
# 			rospy.sleep(0.1)
# 			vel = Twist(Vector3(x_linear, y_linear, z_linear), Vector3(x_angular, y_angular, z_angular))
# 			veloc(vel)


#x = np.linspace(0, 2, 100)

#plt.plot(x, x, label='linear')
#plt.plot(x, x**2, label='quadratic')
#plt.plot(x, x**3, label='cubic')
#plt.show()
          