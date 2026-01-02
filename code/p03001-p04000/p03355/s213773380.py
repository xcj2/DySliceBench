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
a = [i for i in input()]
n = ip()
minplace = [0]
minlet = a[0]
nextlet = 'z'
nextminplace = []
for i in range(1,len(a)):
    if a[i] < minlet:
        nextlet = minlet
        nextminplace = copy.copy(minplace)
        minlet = a[i]
        minplace.clear()
        minplace.append(i)
    elif a[i] == minlet:
        minplace.append(i)
    elif a[i] < nextlet:
        nextminplace.clear()
        nextlet = a[i]
        nextminplace.append(i)
    elif a[i] == nextlet:
        nextminplace.append(i)
wl = []
#print(minplace,nextminplace)
for start in minplace:
    word = [a[start]]
    wl.append(''.join(word))
    for i in range(start+1,start+5):
        if i >= len(a): break
        word.append(a[i])
        wl.append(''.join(word))
wl = list(set(wl))
#print(wl)
for start in nextminplace:
    word = [a[start]]
    wl.append(''.join(word))
    for i in range(start+1,start+5):
        if i >= len(a): break
        word.append(a[i])
        wl.append(''.join(word))
#print(wl)
wl = list(set(wl))
wl.sort()
print(wl[n-1])