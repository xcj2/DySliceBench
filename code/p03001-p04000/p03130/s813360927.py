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

n=nCast(inputArr1(3))


def func():
    if (n[0][0] in n[1] and n[0][0] in n[2]) or (n[0][1] in n[1] and n[0][1] in n[2]):
        return "NO"
    return "YES"
    
print(func()) 


