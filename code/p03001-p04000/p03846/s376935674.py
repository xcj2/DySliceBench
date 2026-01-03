import math
import fractions
import copy
import numpy as np
def j(q):
    if q==1: print("Yes")
    elif q == 0:print("No")
    exit(0)
rem = pow(10,9)+7
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
def printrow(a):
    for i in a:
        print(i)
"""
#decomment when needed
def combinations(n,r):
    if n<r:return 0
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
def permutations(n,r):
    if n<r:return 0
    return math.factorial(n) // math.factorial(n - r)
def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)
"""
n = ip()
a = iprow()
b = sorted(a)
if n%2:
    s = 2
else:
    s = 1
    b.insert(0,0)
if n%2 != 0 and b[0] != 0:
    print(0)
    exit(0)
for i in range(1,n):
    if b[i]!=s:
        print(0)
        exit(0)
    if i%2 == 0:
        s+=2
print(pow(2,n//2,rem))