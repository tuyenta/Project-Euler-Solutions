#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 10:17:23 2019

@author: tuyenta
"""

import time
t=time.time()
def prime_bellow(n):
   b=13
   num=14
   index = 6
   while index<n:
        if all(num%i!=0 for i in range(2,int((num)**0.5)+1)):
            b = num
            index +=1
        num += 1 
   print(b)
prime_bellow(10001)
print(time.time()-t)