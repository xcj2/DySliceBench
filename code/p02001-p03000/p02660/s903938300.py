from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions,copy
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

#素因数分解
def prime_factorize(n):
    if n == 1:
        return [1]
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a
n = inp()
if n == 1:
    print(0)
    quit()
c = Counter(prime_factorize(n))
res = 0
for key in list(c):
    va = c[key]
    cnt = 0
    for i in range(1,100000):
        cnt += i
        if va < cnt:
            res += i-1
            break
print(res)