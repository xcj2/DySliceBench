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
    if n[1]==1:
        return "YES"
    if n[0]%2!=0:
        n[0]=n[0]+1
    if n[1]*2<=n[0]:
        return "YES"
    else:
        return "NO"
    
print(func()) 


