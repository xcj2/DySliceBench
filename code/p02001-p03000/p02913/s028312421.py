from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions
from decimal import Decimal
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

def z_algo(S):
    N = len(S)
    A = [0] * N
    i = 1; j = 0
    A[0] = l = N
    while i < l:
        while i+j < l and S[j] == S[i+j]:
            j += 1
        if not j:
            i += 1
            continue
        A[i] = j
        k = 1
        while l-i > k < j - A[k]:
            A[i+k] = A[k]
            k += 1
        i += k; j -= k
    return A

n = inp()
s = input()
res = 0
for i in range(n-1):
    a = z_algo(s[i:])
    ln = n-i
    for j,x in enumerate(a):
        tmp = min(j,x)
        res = max(res, tmp)
print(res)