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


def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)

count = 0
n= ip()
a = iprow()
currentnum = 1
for i in range(n):
    if currentnum == a[i]:
        currentnum+=1
    else:
        count+=1
if count == n:
    print(-1)
    exit(0)
print(n-currentnum+1)