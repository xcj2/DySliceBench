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


                   
   

def func():
    min=10
    for k in a:
        if k%10!=0 and k%10<min:
            min=k%10
    sum=0
    for k in a:
        if k%10==0:
            sum+=k
        elif min==-1 or k%10!=min:
            sum+=(int(k/10)+1)*10
        else:
    
            sum+=k
            min=-1
    return sum
print(func())
