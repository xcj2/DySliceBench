from collections import Counter
from collections import deque
from functools import reduce
from pprint import pprint
import bisect
import copy
import fractions
import itertools
import math
import queue
import random
import sys
import time
sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def MI(): return map(int, sys.stdin.readline().split())
def II(): return int(sys.stdin.readline())
def IS(): return input()
def C(x): return Counter(x)
def GCD_LIST(numbers): return reduce(fractions.gcd, numbers)
def LCM_LIST(numbers): return reduce(LCM, numbers)
def LCM(m, n): return (m * n // fractions.gcd(m, n))


def f(v, c):
    for next_v, w in graph[v]:
        if seen[next_v] == -1:
            seen[next_v] = (c + w) & 1
            f(next_v, c + w)


n = II()
node = [LI() for _ in range(n - 1)]
graph = [[] for _ in range(n)]
seen = [-1] * n
for u, v, w in node:
    graph[u - 1].append((v - 1, w))
    graph[v - 1].append((u - 1, w))

seen[0] = 0
f(0, 0)
for i in seen:
    print(i)
