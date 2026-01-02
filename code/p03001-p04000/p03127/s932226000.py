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

n=nCast(input())
m=nCast(input().split())



def func():
    s=set(m)
    while len(s)>1:
        l=list()
        for n in s:
            l.append(n)
        l.sort()
        s=set()
        s.add(l[0])
        for n in l:

            k=n%l[0]
     
            if k==1:
                return k
            if k!=0:
                s.add(n%l[0])
    for i in s:
        return i
    

print(func()) 

