# -*- coding:utf-8 -*-
# -*- Python -*-

import sys
import time
sys.path.append(".")
import numpy as np
import math

#def func(x,y,z,th):
x=0
y=0
z=0
th = [1,2,3,4,5,6,7]
P = np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]) #Pの初期化
        
tranX = (x,y,z,th,P)
for i in range(1,7):
    s = math.sin(th[i])
    c = math.cos(th[i])
    if i == 2 or i == 7:
        P = np.array([[1,0,0,x],[0,c,s,y],[0,-s,c,z],[0,0,0,1]])
    elif i == 1 or i == 4 or i == 6:
        P = np.array([[c,0,s,x],[0,1,0,y],[-s,0,c,z],[0,0,0,1]])
    elif i == 3 or i == 5:
        P = np.array([[c,s,0,x],[-s,c,0,y],[0,0,1,z],[0,0,0,1]])
    print P

    

    

    #R7 = tranX(0,0,0,th7)
    #R6 = tranX(0,0,0,th6)
    #R5 = tranX(0,0,0,th5)
    #R4 = tranX(0,0,0,th4)
    #R3 = tranX(0,0,0,th3)
    #R2 = tranX(0,0,0,th2)
    #R1 = tranX(0,0,0,th1)

    #P = R1*R2*R3*R4*R5*R6*R7*Roffset*np.array([[0],[0],[1]])

    #P = np.array([[1,0,0,x],[0,c,s,y],[0,-s,c,z],[0,0,0,1]])

#R1 = Px

#P = R1 * np.array([[0],[0],[0],[1]])
    
#print P



