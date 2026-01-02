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

def func():

    if n[2]-n[1]<2:
        return 1+n[0]
    if n[1]-1>=n[0]:
        return 1+n[0]

    result=n[1]
    ret=n[0]+1-n[1]
 
    if ret%2==0:

        
        return result+int(ret/2)*(n[2]-n[1])
    return 1+result+int((ret-1)/2)*(n[2]-n[1])

print(int(func())) 

