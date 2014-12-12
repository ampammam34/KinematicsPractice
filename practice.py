# -*- coding:utf-8 -*-
# -*- Python -*-

import sys
import time
sys.path.append(".")
import numpy as np
import scipy as sp
import math

#def func(x,y,z,th):
#    P = np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]) #Pの初期化
#    for i in range(7):
#        s = math.sin(th[i])
#        c = math.cos(th[i])


def rotationXandOffset(x, y, z, th):
    th = [0, 0, 0, 0, 0, 0, 0]
    for i in range(7):
        s = math.sin(th[i])
        c = math.cos(th[i])
    P = np.array([[1,0,0,x],[0,c,s,y],[0,-s,c,z],[0,0,0,1]])
    return P

def rotationYandOffset(x, y, z, th):
    th = [0, 0, 0, 0, 0, 0, 0]
    for i in range(7):
        s = math.sin(th[i])
        c = math.cos(th[i])
    P = np.array([[c,0,s,x],[0,1,0,y],[-s,0,c,z],[0,0,0,1]])
    return P

def rotationZandOffset(x, y, z, th):
    th = [0, 0, 0, 0, 0, 0, 0]
    for i in range(7):
        s = math.sin(th[i])
        c = math.cos(th[i])
    P = np.array([[c,s,0,x],[-s,c,0,y],[0,0,1,z],[0,0,0,1]])
    return P

if __name__ == '__main__':
    
    l1 = 10
    l2 = 12
    l3 = 15
    th = [0, 0, 0, 0, 0, 0, 0]
    T = [0]*7

    T1 = rotationYandOffset(0, 0, 0, th[0])
    T2 = rotationXandOffset(0, 0, 0, th[1])
    T3 = rotationZandOffset(0, 0, l1, th[2])
    T4 = rotationYandOffset(0, 0, 0, th[3])
    T5 = rotationZandOffset(0, 0, l2, th[4])
    T6 = rotationYandOffset(0, 0, 0, th[5])
    T7 = rotationXandOffset(l3, 0, 0, th[6])
    
    Hand = np.array([[0],[0],[0],[1]])

    #T = [T1,T2,T3,T4,T5,T6,T7]
    
    #for i in T:
    #    data = sp.dot(Hand,T[i])
    #    i +=1
    #    print data

        
    print sp.dot(sp.dot(sp.dot(T1,T2),sp.dot(T3,T4)),sp.dot(sp.dot(T5,T6),sp.dot(T7,Hand)))
        
    #T = sp.dot(T1,T2,T3,T4,T5,T6,T7,Hand)

    #print 'Hand Positoin is ', T
    

    raw_input();


    #P = R1*R2*R3*R4*R5*R6*R7*Roffset*np.array([[0],[0],[1]])

    #P = np.array([[1,0,0,x],[0,c,s,y],[0,-s,c,z],[0,0,0,1]])

#R1 = Px

#P = R1 * np.array([[0],[0],[0],[1]])
    
#print P



