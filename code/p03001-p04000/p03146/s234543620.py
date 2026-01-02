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

def f(i):
    if i%2==0:
        return i/2
    return i*3+1
def func():
    s=set()
    idx=2
    pre=a
    s.add(a)
    while True:
        
        number=f(pre)
        if number in s:
            return idx
        idx+=1
        s.add(number)
        pre=number

print(func()) 





