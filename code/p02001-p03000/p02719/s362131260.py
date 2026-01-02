import copy

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

def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)

n,k = ips()
a = n//k
b = n//k + 1
a*=k
b*=k
ca = abs(n-a)
cb = abs(n-b)
print(min(ca,cb))