import copy
import heapq

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

n = ip()
a = iprow()
s = [0 for i in range(n+1)]
for i in range(n):
    ans = a[i]
    s[ans] = i+1
for i in range(1,n+1):
    print(s[i],end = "")
    if i!=n:
        print(" ",end  = "")
