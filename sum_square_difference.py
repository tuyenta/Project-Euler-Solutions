#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 10:04:54 2019

@author: tuyenta
"""

def sum_square_difference(n):
    sum_square = 0
    square_sum = 0
    for i in range(1, n+1):
        sum_square += i**2
        square_sum += i
    return square_sum**2 - sum_square

n = 100
print(sum_square_difference(n))    