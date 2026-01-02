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
a=input()
b=input()
c=input()
def func():
    result=0
    for idx in range(0,len(a)):
        if a[idx]==b[idx]==c[idx]:
            result+=0
        elif a[idx]!=b[idx] and a[idx]!=c[idx] and b[idx]!=c[idx]:
            result+=2
        else:
            result+=1
    return result

print(func()) 





