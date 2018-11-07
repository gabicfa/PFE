# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

import numpy as np

Matriz_Pontos=np.array([[1,2,3],[5,5,5],[1,2,0],[12,5,6]])
Pos_Atual=Matriz_Pontos[-1]
Matriz_Oc=[]
lenx=0
leny=0
for i in Matriz_Pontos:
   if i[0] > lenx:
       lenx=i[0]+1
   if i[1] > leny:
       leny=i[1]+1
        
Matriz_Oc=np.zeros((lenx,leny),dtype=int)
      
PosDestino=[0,0,0]

for i in Matriz_Pontos:
    index_x=abs(i[0])
    index_y=abs(i[1])#29.27
    Seccao=Matriz_Oc[index_x]
    Seccao[index_y]+=1
    #break

Vetor=[Matriz_Pontos[-1][0]-PosDestino[0],Matriz_Pontos[-1][1]-PosDestino[1],Matriz_Pontos[-1][2]-PosDestino[2]]

Vetor=-(Vetor/max(Vetor))

Comandos=[]

while (Pos_Atual[0]!=0) and (Pos_Atual[1]!=0):
    while Pos_Atual[0]>0:
        if Matriz_Oc[Pos_Atual[0]-1][Pos_Atual[1]]!=1:
            Pos_Atual[0]-=1
            Comandos.append([-1,0,0])
        else:
            Pos_Atual[1]-=1
            Comandos.append([0,-1,0])
        print(Pos_Atual)
        
    while Pos_Atual[1]>0:
        if Matriz_Oc[Pos_Atual[0]][Pos_Atual[1]-1]!=1:
            Pos_Atual[1]-=1
            Comandos.append([0,-1,0])
        else:
            Pos_Atual[0]-=1
            Comandos.append([-1,0,0])
        print(Pos_Atual)
    while Pos_Atual[0]<0:
        if Matriz_Oc[Pos_Atual[0]+1][Pos_Atual[1]]!=1:
            Pos_Atual[0]+=1
            Comandos.append([1,0,0])
        else:
            Pos_Atual[1]+=1
            Comandos.append([0,1,0])
        print(Pos_Atual)
        
    while Pos_Atual[1]<0:
        if Matriz_Oc[Pos_Atual[0]][Pos_Atual[1]+1]!=1:
            Pos_Atual[1]+1
            Comandos.append([0,1,0])
        else:
            Pos_Atual[0]+=1
            Comandos.append([1,0,0])
        print(Pos_Atual)

