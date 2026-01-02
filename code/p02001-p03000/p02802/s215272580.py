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


n,m = ips()
correct = [0 for i in range(n+1)]
wasu = [0 for i in  range(n+1)]
for loop in range(m):
    q,r = input().split()
    q = int(q)
    if r == "WA":
        if correct[q]==0:
            wasu[q]+=1
    else:
        correct[q] = 1
allwa = 0
for i in range(len(correct)):
    if correct[i]:
        allwa+=wasu[i]
print(sum(correct),allwa)