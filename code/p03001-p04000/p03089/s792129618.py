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
ans = []
for i in range(n):
    for p in range(len(a)-1,-1,-1):
        if p+1 == a[p]:
            ans.insert(0,p+1)
            a.pop(p)
            break
if len(a):
    print(-1)
else:
    for i in ans:
        print(i)
