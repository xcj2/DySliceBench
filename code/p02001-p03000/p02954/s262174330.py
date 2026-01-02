import copy
import heapq
import math
import fractions

def j(n):
    if n:print("Yes")
    else:print("No")
    exit(0)
rem = 10 ** 9 + 7

"""
def ct(x,y):
    if (x>y):print("+")
    elif (x<y): print("-")
    else: print("?")
"""

def ip():
    return int(input())
def iprow():
    return [int(i) for i in input().split()]
def ips():
    return (int(i) for i in input().split())
def ipmultiplerow(n):
    a = []
    for i in range(n):
        a.append(ip())
    return a
def printrow(a):
    for i in a:
        print(i)
def printlist(a):
    for i in range(len(a)-1):
        print(a[i],end = " ")
    print(a[-1])

a = input()
l = len(a)
s = [0 for i in range(len(a))]
ct = 0
intersect = 0
#print(l)
for i in range(l):
    if a[i] == 'L':
        ct+=1
        s[i] = intersect+ct%2
    else:
        ct = 0
        intersect = i
for i in range(l-1,-1,-1):
    if a[i] == 'R':
        ct += 1
        s[i] = intersect - ct % 2
    else:
        ct = 0
        intersect = i
#printlist(s)
b = [0 for i in range(l)]
for i in s:
    b[i]+=1
printlist(b)