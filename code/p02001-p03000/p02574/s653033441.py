from math import ceil,floor,factorial,gcd,sqrt,log2,cos,sin,tan,acos,asin,atan,degrees,radians,pi,inf
from itertools import accumulate,groupby,permutations,combinations,product,combinations_with_replacement
from collections import deque,defaultdict,Counter
from bisect import bisect_left,bisect_right
from operator import itemgetter
from heapq import heapify,heappop,heappush
from queue import Queue,LifoQueue,PriorityQueue
from copy import deepcopy
from time import time
from functools import reduce, lru_cache
import string
import sys
sys.setrecursionlimit(10 ** 7)
def input() : return sys.stdin.readline().strip()
def INT()   : return int(input())
def MAP()   : return map(int,input().split())
def MAP1()  : return map(lambda x:int(x)-1,input().split())
def LIST()  : return list(MAP())
def LIST1() : return list(MAP1())

n = INT()
a = LIST()
m = max(a)

primes = [0]*(m+1)
primes[1] = 1
for i in range(2, m+1):
    if primes[i] == 0:
        for j in range(1, m//i+1):
            primes[i*j] = i

count = [0]*(m+1)
for x in a:
    y = x
    while primes[y] != y:
        count[primes[y]] += 1
        p = primes[y]
        while y % p == 0:
            y //= p
    if primes[y] >= 2:
        count[primes[y]] += 1

if max(count) <= 1:
    print("pairwise coprime")
else:
    g = 0
    for x in a:
        g = gcd(g, x)
    if g == 1:
        print("setwise coprime")
    else:
        print("not coprime")