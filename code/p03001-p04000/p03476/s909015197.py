import sys
import math
import itertools
import bisect
from copy import copy
from collections import deque,Counter
from decimal import Decimal
def s(): return input()
def i(): return int(input())
def S(): return input().split()
def I(): return map(int,input().split())
def L(): return list(input().split())
def l(): return list(map(int,input().split()))
def lcm(a,b): return a*b//math.gcd(a,b)
sys.setrecursionlimit(10**9)
INF = 10**9
mod = 10**9+7

def era(n):
    primes = [0, 1] * (n // 2 + 1)
    if n % 2 == 0:
        primes.pop()
    primes[1] = 0
    primes[2] = 1
    for p in range(3, n + 1, 2):
        if primes[p]:
            for q in range(p * p, n + 1, 2 * p):
                primes[q] = 0
    return primes

Q = i()
primes = []
l1 = era(100000)
for l in range(len(l1)):
    if l1[l] == 1:
        primes.append(l)
l2 = []
for l in primes:
    if (l+1)//2 in primes:
        l2.append(l)
for i in range(Q):
    l,r = I()
    print(bisect.bisect_right(l2,r)-bisect.bisect_left(l2,l))