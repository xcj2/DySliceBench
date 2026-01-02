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

def Z_algorithm(s):
    n = len(s)
    Z = [0]*n
    Z[0] = n
    i,j = 1,0
    while i < n:
        while i+j < n and s[j] == s[i+j]:
            j += 1
        Z[i] = j
        if j == 0:
            i += 1
            continue
        k = 1
 
        #再利用部分
        while i+k < n and k+Z[k] < j:
            Z[i+k] = Z[k]
            k += 1
        i += k
        j -= k
    return Z

n = I()
a = LI()
b = LI()

x = [a[i%n]^a[(i+1)%n] for i in range(2*n)]
y = [b[i%n]^b[(i+1)%n] for i in range(n)]
z = Z_algorithm(y+x)
for i in range(n,2*n):
    if z[i] >= n:
        k = i-n
        x = a[k] ^ b[0]
        print(k,x)
