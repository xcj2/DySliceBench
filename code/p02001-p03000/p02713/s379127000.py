import bisect, collections, copy, heapq, itertools, math, string
from functools import reduce
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

def gcd(*numbers):
    return reduce(math.gcd, numbers)

K = I()
ans = 0
for i in range(1, K + 1):
    for j in range(1, K + 1):
        for k in range(1, K + 1):
            ans += gcd(i, j, k)
print(ans)