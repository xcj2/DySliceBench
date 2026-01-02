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
 
n=int(input())
a=nCast(inputArr(5))


                   
   

def func():
    mm=min(a)
    k=0
    if n%mm!=0:
        k=1
    k+=int(n/mm)+4
    return k
print(func())
