# -*- coding: utf-8 -*-
"""
Spyderエディタ

これは一時的なスクリプトファイルです
"""

import math
import copy
import bisect
def nCast(number):
    if type(number)==str:
        return int(number)
    for idx in range(0,len(number)):
        if type(number[idx])==str:
 
            number[idx]=int(number[idx])
        else:
            nCast(number[idx])
    return number
    
def inputArr(w):
    l=list()
    for idx in range(0,w):
        l.append(input())
    return l
def inputArr1(w):
    l=list()
    for idx in range(0,w):
        l.append(input().split())
    return l
 
n=input()
 
 
 
def func():
    if n<="2019/04/30":
        return "Heisei"
    return "TBD"
 
 
print(func()) 