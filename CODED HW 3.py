#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 22:22:07 2018

@author: Pir8
"""

#Problem 1:
#Create a function scale_rotate(S, k, theta) that scales the points in the input set  SS  by a factor of  kk  and rotates them by  θθ  degrees, where  θθ  is a multiple of  90∘90∘ . The function should satisfy the following:
#
#INPUT:
#S - set S
#k - positive float, if negative or zero factor is given then the function displays error message, "ERROR: Scaling factor must be a positive float".
#theta - a float. If theta is positive, rotation is counterclockwise, else it is clockwise.
#OUT:
#T - set T consisting of points in S scaled by  kk  and rotated by  θθ

from plotting import plot
import math

def scale_rotate(S, k, theta):
    if k > 0:
        T = {k * x for  x in S}
        rad = (theta / 180) * math.pi
        n = theta // 90
        if theta % 90 == 0 and theta > 0:  
            T = {(1j ** n)*z for z in S}  
        elif theta % 90 == 0 and theta < 0:
            T = {((-1j) ** n)*z for z in S} 
    else:
        print("ERROR: Scaling factor must be a positive float")
    return T
#
#S = {2 + 2j, 3 + 2j, 1.75 + 1j, 2 + 1j, 2.25 + 1j, 2.5 + 1j, 2.75 + 1j, 3 + 1j, 3.25 + 1j}
#R = scale_rotate(S, 3, 72)
#plot(S, 4)
#plot(R, 4)

from plotting import plot
import cmath

def polar(z):
    if z == z.real + z.imag*1j:
        r = cmath.sqrt((z.real)**2 + (z.imag*1j)**2)
        degTheta = cmath.atan((z.imag*1j)/(z.real))
        theta = (degTheta * cmath.pi) / 180
    else:
        print("ERROR: Input must be complex")
    return (r, theta)


polar(3 + 2j)
plot(polar(3 + 2j), 4)


#def scale_rotate(S, k, tau):
#    if(k <= 0):
#        print("ERROR: Scaling factor must be a positive float")
#    else:
#        if(tau > 0):
#            T = {k ** (tau * (1 +2j)) for z in S} 
#        elif(tau <= 0):
#            T = {k ** (tau * (-1 -2j)) for z in S} 
#    return T  
#  
#from plotting import plot
#import math
#S = {2 + 2j, 3 + 2j , 1.75 + 1j, 2 + 1j, 2.25 + 1j, 2.5 + 1j, 2.75 + 1j, 3 + 1j, 3.25 + 1j}
#
#T = scale_rotate(S, 0.5, math.pi)
#plot(T, 6)
#plot(S, 6)

#from image import file2image
#from plotting import plot
#T = file2image("img01.png")
#row = 0
#data = []
#for x in T:
#    col = 0
#    for y in x:
#        if y[0] < 120:
#            data.append([col, row])
#        col +=1
#    row += 1
#isImaginaryNum = False
#real = 0
#imaginaryNum = 1j
#dataList = []
#for a in data:
#    for b in a:
##        if isImaginaryNum == False:
##            real = b
##            isImaginary = True
#        if isImaginaryNum == True:            
#            imaginaryNum = b * 1j
#            isImaginaryNum = False
#        elif isImaginaryNum == False:
#            real = b
#            isImaginary = True
#    S = real + imaginaryNum
#    dataList.append(S)
#CData = scale_rotate(dataList, 1, 180)
#realData = []
#for m in CData:
#    realData.append(m + 200 + 200j)
#
#plot(realData, 200)

#from image import file2image
#from plotting import plot
#T = file2image("img01.png")
#row = 0
#pts = []
#for x in T:
#    column = 0
#    for y in x:
#        if y[0] < 120:
#            pts.append([column, row])
#        column +=1
#    row += 1
#isImaginary = False
#real = 0
#imaginary = 1j
#points = []
#for a in pts:
#    for b in a:
#        if isImaginary == False:
#            real = b
#            isImaginary = True
#        elif isImaginary == True:            
#            imaginary = b*1j
#            isImaginary = False
#    Z = real + imaginary
#    points.append(Z)
#Cpoints = scale_rotate(points, 1, 180)
#truePoints = []
#for m in Cpoints:
#    truePoints.append(m + 200 + 200j)
#
#plot(truePoints, 200)

from image import file2image
from plotting import plot

T = file2image("img01.png")
row = 0
data = []
for x in T:
    col = 0
    for y in x:
        if y[0] < 120:
            data.append([col, row])
        col +=1
    row += 1
isImaginaryNum = False
real = 0
imaginaryNum = 1j
dataList = []
for a in data:
    for b in a:
        if isImaginaryNum == True:            
            imaginaryNum = b * 1j
            isImaginaryNum = False
        elif isImaginaryNum == False:
            real = b
            isImaginary = True
    S = real + imaginaryNum
    dataList.append(S)
CData = scale_rotate(dataList, 1, 180)
realData = []
for m in CData:
    realData.append(m + 200 + 200j)

plot(realData, 200)