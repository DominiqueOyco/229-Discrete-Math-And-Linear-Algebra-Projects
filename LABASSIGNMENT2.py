#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 09:44:27 2018

@author: Pir8
"""

def binaryProd(a,b):
    n = len(a)
    m = len(b)
    deca = 0
    decb = 0
    ita = n-1
    itb = m-1
    
    for j in range (n-1, -1, -1):
        exp = (n - 1) - ita
        if a[j] == ' ':
            pass
        else:
            deca += 2 ** (exp) if a[j] == '1' else 0
            ita -= 1
        
    for k in range (m-1, -1, -1):
        exp = (m -1) - itb
        if b[k] == ' ':
            pass
        else:
            decb += 2 ** (exp) if b[k] == '1' else 0
            itb -= 1
            
    total = int(deca * decb)   
    bintotal = ''
    iterator = 1
    
    while total != 0:
        r = total % 2
        bintotal = ('1' + bintotal) if r == 1 else ('0' + bintotal)
        if (iterator%4 == 0):
            bintotal = ' ' + bintotal
        total = int(total / 2)
        iterator += 1
    return bintotal

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
    finalx = 1
    y = 1
    finaly = 0
    b1 = b
    a1 = a

    while b1 != 0:
        quotient = int(a1/b1)
        
        #this will solve the value of a1 and b1 then swamp them
        #a1 will hold the current b1, b1 will use current a1
        #then the values will update to their values
        a1, b1 = b1, a1 - quotient*b1
        finalx, x = x, finalx - quotient*x
        finaly, y = y, finaly - quotient*y

    return [finalx, finaly]

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
