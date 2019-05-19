#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 09:44:27 2018

@author: Pir8
"""

def binaryProd(a,b):
    x = len(a)
    y = len(b)
    deca = 0
    decb = 0
    ita = x-1
    itb = y-1
    
    for j in range (x-1, -1, -1):
        exp = (x - 1) - ita
        if a[j] == ' ':
            pass
        else:
            deca += 2 ** (exp) if a[j] == '1' else 0
            ita -= 1
        
    for k in range (y-1, -1, -1):
        exp = (y -1) - itb
        if b[k] == ' ':
            pass
        else:
            decb += 2 ** (exp) if b[k] == '1' else 0
            itb -= 1
            
    total = int(deca * decb)   
    p = ''
    iterator = 1
    
    while total != 0:
        r = total % 2
        p = ('1' + p) if r == 1 else ('0' + p)
        if (iterator%4 == 0):
            p = ' ' + p
        total = int(total / 2)
        iterator += 1
    return p

print(binaryProd("1 0100" ,  "111 0111"))

"""
LOOKING FOR THE PRIMES
"""

def primeFactors(a):
    i = 2               
    l = []              #The list of prime factors
    while i * i <= a: 
        if a % i:
            i += 1
        else:
            a //= i
            l.append(i)
    if a > 1:
        l.append(a)
    return l
print(primeFactors(60))


"""
GET THE BEZOUT COEFFICIENTS
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
        
        #this will solve the value of a1 and b1 then swamp them
        #a1 will hold the current b1, b1 will use current a1
        #then the values will update to their values
        a0, b0 = b0, a0 - quotient * b0
        lastX, x = x, lastX - quotient * x
        lastY, y = y, lastY - quotient * y

    return (lastX, lastY)

print(bezoutCoeffs(414, 662))

"""
GET THE COMMON GCD OF A AND B
"""

def gcd(a,b):
    d = 0
    while b:
        a, b = b, a % b
        d = a
    return d

print(gcd(414, 662))
