'''
Created on 2019年3月3日

@author: zcg01
'''
import math
import copy
 
 
 
 
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
        l.append(input())
    return l
 
a=nCast(input().split());
b=nCast(input().split());
 

 
def func():

    return (a[0]-b[0])*(a[1]-b[1])
print(func()) 