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
def combinations(n,r):
    if n<r:return 0
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
def permutations(n,r):
    if n<r:return 0
    return math.factorial(n) // math.factorial(n - r)
def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)
x,y = ips()
a = []
for i in range(x):
    a.append(iprow())
ans=0
for i in range(x):
    p = a[i]
    for k in range(i+1,x):
        q = a[k]
        s = 0
        for l in range(y):
            s+=pow(p[l]-q[l],2)
        if math.sqrt(s) == int(math.sqrt(s)):
            ans+=1
print(ans)