import sys
sys.setrecursionlimit(300000)
from math import sqrt, ceil
from collections import defaultdict

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def MI0(): return map(lambda s: int(s) - 1, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
def LMI0(): return list(map(lambda s: int(s) - 1, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


N = I()

n = ceil(sqrt(N))
d = defaultdict(int)
for x in range(1, n + 1):
    for y in range(1, n + 1):
        for z in range(1, n + 1):
            a = x ** 2 + y ** 2 + z ** 2 + x * y + y * z + z * x
            if a <= N:
                d[a] += 1
for i in range(1, N + 1):
    print(d[i])