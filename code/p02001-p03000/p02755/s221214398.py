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

a,b = ips()

for i in range(1001):
    if int(i*0.08) == a and int(i*0.1) == b:
        print(i)
        exit(0)
print(-1)