
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
 
a=nCast(input().split());

b=nCast(inputArr1(a[0]))


def bkey(n):
    return n[0]
 
def func():
    b.sort(key=bkey)
    sum=0
    count=0
    for idx in range(0,len(b)):

        if count+b[idx][1]<a[1]:
            count+=b[idx][1]
            sum+=b[idx][0]*b[idx][1]
        else:
            sum+=b[idx][0]*(a[1]-count)
            return sum
    return sum
    
print(func()) 