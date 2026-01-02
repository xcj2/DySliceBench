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

n=nCast(input())
a=nCast(input().split())
b=nCast(input().split())
c=list()
def func():
    result=0
    if sum(a)<sum(b):
        return -1
    for idx in range(0,len(a)):
        c.append(a[idx]-b[idx])
    c.sort()
    need=0
    result=0

    for number in c:
        if number<0:
            need+=number
            result+=1
        else:
            break

    if need==0:
        return 0
    for number in reversed(c):
        result+=1
        need+=number
        if need>=0:
            break
    return result

print(func()) 
