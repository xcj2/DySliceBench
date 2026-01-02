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
b = str(n)
a = [int(i) for i in b]
if n <10:
    print(n)
    exit(0)
backup = copy.copy(a)
ans = sum(a)
for i in range(len(a)-1):
    if a[i] != 9:
        a[i]-=1
        for k in range(i+1,len(a)):
            a[k] = 9
ans = max(ans,sum(a))
#print(a,sum(a))
l = len(a)
if a[l-1] != 9:
    a[l-1] = 9
    a[l-2] -=1
#print(a,sum(a))
ans = max(ans,sum(a))
a = copy.copy(backup)
for i in range(1,len(a)-1):
    if a[i] != 9:
        a[i-1]-=1
        for k in range(i,len(a)):
            a[k] = 9
ans = max(ans,sum(a))
print(ans)

