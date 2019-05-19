#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 11:33:52 2018

@author: Pir8
"""

def binaryAdd(a,b):
        n = max(len(a), len(b)) #the length of the given string for a and b
        a = a.zfill(n)          #balances both a and b by adding 0's in the front
        b = b.zfill(n)          #balances both a and b by adding 0's in the front
        c = 0                   #carry
        s = ''

        for j in range(n-1, -1, -1):
            r = c
            r += 1 if a[j] == '1' else 0
            r += 1 if b[j] == '1' else 0
            s = ('1' if r % 2 == 1 else '0') + s
            c = 0 if r < 2 else 1       

        if c !=0 : s = '1' + s

        return s.zfill(n)
    
print(binaryAdd("10101", "101011"))
print(binaryAdd("101", "111"))
