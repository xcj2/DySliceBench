import sys
import math
import numpy as np
from collections import Counter, defaultdict, deque
import itertools

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def S():
    return input().rstrip()


def I():
    return int(input())


def MI():
    return map(int, input().split())


inf = float("inf")
mod = 10 ** 9 + 7

n, m = MI()
d = defaultdict(set)
for _ in range(m):
    a, b = MI()
    d[a].add(b)
    d[b].add(a)

li = list(range(2, n + 1))

ans = 0
for l in itertools.permutations(li):
    now = 1
    for i, next in enumerate(l):
        if next in d[now]:
            now = next
            if i == n - 2:
                ans += 1
        else:
            break

print(ans)
