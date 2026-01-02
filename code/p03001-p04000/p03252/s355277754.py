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
cv = "abcdefghijklmnopqrstuvwxyz"
convert = [cv[i] for i in range(26)]
s = input()
t = input()
a = [convert.index(s[i]) for i in range(len(s))]
b = [convert.index(t[i]) for i in range(len(t))]
c = [[] for i in range(26)]
d = [[] for i in range(26)]

for i in range(len(a)):
    c[a[i]].append(b[i])
for i in range(len(b)):
    d[b[i]].append(a[i])
for i in range(26):
    if len(set(c[i]))>1 or len(set(d[i]))>1:j(0)
j(1)