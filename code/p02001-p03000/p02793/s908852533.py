#!/usr/bin/env python3

import sys
import math
from bisect import bisect_right as br
from bisect import bisect_left as bl
sys.setrecursionlimit(2147483647)
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

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append((i, cnt))

    if temp!=1:
        arr.append((temp, 1))

    if arr==[]:
        arr.append((n, 1))

    return arr

n = I()
a = LI()
lst = [0]*(10**6+1)
for i in a:
    l = factorization(i)
    for (j,k) in l:
        lst[j] = max(lst[j],k)

t = 1
for i in range(1,10**6+1):
    if lst[i] != 0:
        t = t*(i**lst[i]) % mod
ans = 0
for i in a:
    ans += t*pow(i,mod-2,mod) % mod
    ans %= mod
print(ans)