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
a = []
for i in range(5):
    a.append(ip())
if min(a)>=n:
    print(5)
    exit(0)
ans = n//min(a)
if n%min(a):
    ans+=1
print(ans+4)