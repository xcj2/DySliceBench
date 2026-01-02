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

n=nCast(input().split())
def func():
    res1=min(n[1],n[2])
    if n[1]+n[2]<=n[0]:
        res2=0
    else:
        res2=res2=n[1]+n[2]-n[0]
    return str(res1)+" "+str(res2)


print(func()) 





