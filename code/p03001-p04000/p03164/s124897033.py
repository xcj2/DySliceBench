from decimal import *
from bisect import bisect_left as bl
from bisect import bisect_right as br
from heapq import heappush,heappop
import math
from collections import *
from functools import reduce,cmp_to_key
import sys
input = sys.stdin.readline

M = mod = 998244353
def factors(n):return sorted(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))
def inv_mod(n):return pow(n, mod - 2, mod)

def li():return [int(i) for i in input().rstrip('\n').split()]
def st():return input().rstrip('\n')
def val():return int(input().rstrip('\n'))
def li2():return [i for i in input().rstrip('\n')]
def li3():return [int(i) for i in input().rstrip('\n')]
def li4():return [float(i) for i in input().rstrip('\n').split(' ')]

n,w = li()
l = []
for i in range(n):l.append(li())
l.sort()
d = defaultdict(int)
for i in range(10**5 + 10):d[i] = float('inf')
for i in l:

    for j in range(10 ** 5 + 10,0,-1):
        d[j + i[1]] = min(d[j + i[1]],d[j] + i[0])
    d[i[1]] = min(d[i[1]],i[0])
ans = 0
for i in range(10**5 + 10):
    if d[i] <= w:ans = i
print(ans)

