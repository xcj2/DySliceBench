#!/usr/bin/env python3
#ABC142 D

import sys
import math
from bisect import bisect_right as br
from bisect import bisect_left as bl
sys.setrecursionlimit(1000000000)
from heapq import heappush, heappop,heappushpop
from collections import defaultdict
from itertools import accumulate
from collections import Counter
from collections import deque
from operator import itemgetter
from itertools import permutations
mod = 10**9 + 7
inf = float('inf')
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
        
    return divisors

def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]

def gcd(n,m):
    if m == 0:
        return n
    else:
        return gcd(m,n % m)

P = [1] + primes(10**6)
f = defaultdict(lambda : 0)
for i in P:
    f[i] = 1
a,b = LI()
A,B = make_divisors(a),make_divisors(b)
ans = 0
fa = defaultdict(lambda : 0)
fb = defaultdict(lambda : 0)

for i in A:
    fa[i] = 1
for i in B:
    fb[i] = 1

ans = 0
lst = []
p = []
for i in A:
    if fa[i] and fb[i]:
        if f[i]:
            ans += 1
            p.append(i)
        else:
            lst.append(i)
for i in lst:
    for j in p:
        if gcd(i,j) != 1:
            break
    else:
        ans += 1
print(ans)




