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
        l.append(input())
    return l

a=nCast(input())
b=nCast(input().split())


def help(max):
    count=0
    tmp=0
    for idx in range(0,len(b)):
        if b[idx]==max:
            b[idx]=b[idx]-1
            if tmp==0:
                tmp=1
        else:
            if tmp==1:
                tmp=0
                count+=1

    return tmp+count

def func():
    result=0
    max=100
    while max!=0:
        result+=help(max)
        max-=1
    return result
print(func()) 





