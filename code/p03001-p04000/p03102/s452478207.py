
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
b=nCast(input().split());
c=nCast(inputArr1(a[0]));

 
def func():
    result=0
    for number in c:
        sumall=0
        for idx in range(0,len(number)):
            sumall+=number[idx]*b[idx]
        if sumall+a[2]>0:
            result+=1
    return result
print(func()) 