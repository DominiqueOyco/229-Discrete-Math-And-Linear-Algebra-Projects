#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 22:58:19 2018

@author: Pir8
"""

def bezoutCoeffs(a, b):
    x = 0
    lastX = 1
    y = 1
    lastY = 0
    b0 = b
    a0 = a

    while b0 != 0:
        quotient = int(a0/b0)
        a0, b0 = b0, a0 - quotient * b0
        lastX, x = x, lastX - quotient * x
        lastY, y = y, lastY - quotient * y

    return lastX

def decryptRSA(c, p, q, e):
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    digits2letters = {"00" : "A", "01" : "B", "02" : "C", "03" : "D", "04" : "E",
                      "05" : "F", "06" : "G", "07" : "H", "08" : "I", "09" : "J",
                      "10" : "K", "11" : "L", "12" : "M", "13" : "N", "14" : "O",
                      "15" : "P", "16" : "Q", "17" : "R", "18" : "S", "19" : "T",
                      "20" : "U", "21" : "V", "22" : "W", "23" : "X", "24" : "Y",
                      "25" : "Z"}  
    numberSize = len(c)
    
    letterList = []
        
    for i in range(0, numberSize , 1):
        letterList.append(numbers.index(c[i]))
        
    letterSize = len(letterList)
    stringList =[]
    
    for j in range(0, letterSize - 1, 2):
        if letterList[j] < 10:
            if letterList[j + 1] < 10:
                stringList.append('0' + str(letterList[i]) + '0' + str(letterList[j + 1]))
            else:
                stringList.append('0' + str(letterList[i]) + str(letterList[j + 1]))
        elif numbers[j + 1] < 10:
            stringList.append(str(letterList[j]) + '0' + str(letterList[j + 1]))
        else:
            stringList.append(str(letterList[j]) + str(letterList[j + 1]))
            
    decrypted = ''
    
    for k in range(0, len(stringList), 1):
        s = (int(stringList[k]) ** e) % ((p - 1) * (q - 1))
        sString = ''
        if s < 10:
            sString = '000' + str(s)
        elif s < 100:
            sString = '00' + str(s)
        elif s < 1000:
            sString = '0' + str(s)        
        else:
            sString = str(s)
#            charStr = list(sString)           
        decrypted = decrypted + sString
        nums = decrypted
        decryptedMessage = "";
        
        for l in range(0, len(nums), 2):
            decryptedMessage += digits2letters[nums[l : l + 2]]
        
        
    return(decryptedMessage)
    
    
def encryptDSRSA(m, p, q, e):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
               'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
               'U', 'V', 'W', 'X', 'Y', 'Z']
    alphabetSize = len(m)
    numList = []
    
    for i in range(0, alphabetSize, 1):
        numList.append(alphabet.index(m[i]))
        
    numSize = len(numList)
    stringList =[]
    
    for j in range(0, numSize - 1, 2):
        if numList[j] < 10:
            if numList[j + 1] < 10:
                stringList.append('0' + str(numList[j]) + '0' + str(numList[j + 1]))
            else:
                stringList.append('0' + str(numList[j]) + str(numList[j + 1]))
        elif numList[j + 1] < 10:
            stringList.append(str(numList[j]) + '0' + str(numList[j + 1]))
        else:
            stringList.append(str(numList[j]) + str(numList[j + 1]))
            
    encryptedMessage = ''
    
    for k in range(0, len(stringList), 1):
        c = (int(stringList[k]) ** e) % (p * q)
        cString = ''
        if c < 10:
            cString = '000' + str(c)
        elif c < 100:
            cString = '00' + str(c)
        elif c < 1000:
            cString = '0' + str(c)        
        else:
            cString = str(c)
        encryptedMessage = encryptedMessage + cString
    return(encryptedMessage)
    

print(decryptRSA('09810461', 43, 59, 13))  
print(decryptRSA('066719470671', 43, 59, 13))  
print(encryptDSRSA('STOP', 43, 59, 13))
print(encryptDSRSA('NIGHT', 43, 59, 13))