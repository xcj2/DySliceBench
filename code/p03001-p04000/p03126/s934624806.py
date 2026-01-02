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

n=nCast(input().split())
m=nCast(inputArr1(n[0]))



def func():
    
    s=set(m[0][1:])
    for mm in m:
        tmp=set(mm[1:])
        s=s&tmp
    return len(s)
        


print(func()) 

