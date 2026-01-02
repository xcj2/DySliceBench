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
a,b,c,x,y = ips()
c*=2
z = 0
sum = x*a+b*y
cm = sum
while x and y:
    x-=1
    y-=1
    z+=1
    sum-=(a+b)
    sum+=c
    cm = min(cm,sum)
if x:
    while x>0:
        x-=1
        sum-=a
        sum+=c
        cm = min(cm,sum)
elif y:
    while y>0:
        y -= 1
        sum -= b
        sum += c
        cm = min(cm, sum)
print(cm)