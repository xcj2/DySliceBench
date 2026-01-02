import sys
sys.setrecursionlimit(300000)
from math import gcd
from collections import defaultdict

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


K = I()
memo = dict()

def g(a, b):
    if a > b:
        a, b = b, a
    if memo.get((a, b)) is not None:
        return memo[(a, b)]
    else:
        val = gcd(a, b)
        memo[(a, b)] = val
        return val

d = defaultdict(int)
for b in range(1, K + 1):
    for c in range(1, K + 1):
        d[g(b, c)] += 1

ans = 0
for a in range(1, K + 1):
    for val, cnt in d.items():
        ans += g(a, val) * cnt
print(ans)
