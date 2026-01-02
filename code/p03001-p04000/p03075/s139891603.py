import math
import copy
from collections import Counter
from _ast import Or
 
 
 
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
 

a=nCast(inputArr(5))
b=int(input())

                   
   

def func():
    global a
    for idx in range(len(a)):
        for idy in range(idx+1,len(a)):
            k=a[idx]-a[idy]
            if(b<abs(k)):
                return ":("
    return "Yay!"
print(func())
