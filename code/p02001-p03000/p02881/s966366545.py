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
def printmultiplerow(a):
    for i in a:
        print(i)
def printrow(a):
    for i in range(len(a)-1):
        print(a[i],end = " ")
    print(a[-1])


n = ip()
p = int(math.sqrt(n))
ans = n-1
for i in range(1,p+1):
    if n%i==0:
        l = n//i
        ans  = l+i-2
print(ans)
