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
x,y = ips()

if x%3==0 or y%3 == 0:
    print(0)
    exit(0)
ans = min(x,y)
base = [y,y//2,y//2]
if y%2:base[2]+=1
total = [0,x*base[1],x*base[2]]
ans = min(ans,max(total)-min(total))
for i in range(x):
    total[0]+=y
    total[1]-=base[1]
    total[2]-=base[2]
    ans = min(ans,max(total)-min(total))

base = [x,x//2,x//2]
if x%2:base[2]+=1
total = [0,y*base[1],y*base[2]]
ans = min(ans,max(total)-min(total))
for i in range(y):
    total[0]+=x
    total[1]-=base[1]
    total[2]-=base[2]
    ans = min(ans,max(total)-min(total))
print(ans)



