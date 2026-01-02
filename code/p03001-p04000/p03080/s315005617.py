import math
import copy
from collections import Counter
 
 
 
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
 

a=(input())
b=input()


def func():
    if b.count("R")>len(b)/2:
        return "Yes"
    return "No"
 
print(func())
