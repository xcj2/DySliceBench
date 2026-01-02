from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n,k = inpl()
a = inpl()
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort(reverse = True)
    return divisors
pr = make_divisors(sum(a))
def sol(p):
    mo = []
    pl = []
    for i in a:
        if i%p != 0:
            mo += [i%p]
            pl += [p-i%p]
    mo.sort(); pl.sort()
    m = 0; c = sum(pl)
    ln = len(mo)
    for i in range(ln):
        m += mo[i]
        c -= pl[ln-i-1]
        if max(m,c) <= k and m%p == c%p:
            return True
    return False
for p in pr:
    if sol(p):
        res = p
        break
else:
    res = 1
print(res)

