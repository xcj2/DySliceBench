# -*- coding: utf-8 -*-
def inpl(): return map(int, input().split())
from itertools import accumulate
from bisect import bisect, bisect_left
from collections import Counter, deque
from functools import reduce
from itertools import accumulate
from operator import itemgetter, xor

from sys import setrecursionlimit
setrecursionlimit(10**9)
 
import sys
#input = sys.stdin.readline
from collections import Counter
def inpl(): return list(map(int, input().split()))

N, K = inpl()
A = inpl()

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    # divisors.sort()
    return divisors

D = sorted(make_divisors(sum(A)))

ans = 1
g0 = itemgetter(0)

for d in D:
    x = 0
    X = []
    for i in range(N):
        X.append(A[i]%d)

    X = sorted(X)
    l = 0
    r = N-1
    while l < N and X[l] == 0:
        l += 1
    while l < N and (not (X[l] == 0 or X[l] == d)):
        m = min(X[l], d - X[r])
        x += m
        X[l] -= m
        X[r] += m
        if X[l] == 0:
            l += 1
        if X[r] == d:
            r -= 1
    if x <= K:
        ans = max(ans, d)

print(ans)