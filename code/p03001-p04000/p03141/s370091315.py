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
        l.append(input().split())
    return l

n=nCast(input())
a=nCast(inputArr1(n))

def akey(a):
    return a[0]+a[1]
list.sort(a,key=akey,reverse=True)


def func(a):
    pa,pb=0,0
    tag=True
    for idx in range(0,len(a)):
        if tag:
            pa+=a[idx][0]
        else:
            pb+=a[idx][1]
        tag=not tag
    return pa-pb
    
print(func(a)) 





