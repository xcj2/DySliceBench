import math
import fractions
import copy
import numpy as np
def j(q):
    if q==1: print("YES")
    elif q == 0:print("NO")
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
a  = iprow()
ans = sum(a)
b = iprow()
pl = 0
pr = n-1
if n==1:
    print(min(sum(b),sum(a)))
    exit(0)

while pl <= pr:
    if b[pl] - a[pl]>0:
        b[pl] -= a[pl]
        a[pl] = 0
    else:
        a[pl]-=b[pl]
        b[pl] = 0
    if b[pl]:
        if b[pl] - a[pl+1]>0:
            b[pl] = 0
            a[pl+1] = 0
        else:
            a[pl+1]-=b[pl]
            b[pl] = 0
    if b[pr] - a[pr+1] > 0:
        b[pr] -= a[pr + 1]
        a[pr+1] = 0
    else:
        a[pr+1] -= b[pr]
        b[pr] = 0
    if b[pr]:
        if b[pr] - a[pr] > 0:
            a[pr] = 0
            b[pr] = 0
        else:
            a[pr] -= b[pr]
            b[pr] = 0
    pl+=1
    pr-=1
print(ans-sum(a))