from collections import Counter
from functools import reduce
# import statistics
import bisect
import copy
import fractions
import math
import pprint
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
def GCD_LIST(numbers):
    return reduce(fractions.gcd, numbers)
def LCM_LIST(numbers):
    return reduce(LCM, numbers)
def LCM(m, n):
    return (m * n // fractions.gcd(m, n))
def unite(x, y):
    # それぞれのノードの根を求める
    x = root(x)
    y = root(y)
    if x == y:
        return
    # node[x]の根をyに変更する
    node[x] = y
def same(x,y): return bool(root(x) == root(y))
def root(x):
    if node[x] == x:  # xが根の場合
        return x
    else:
        node[x] = root(node[x])  # 経路圧縮
        return node[x]
def dfs(v,depth):
    # ノードに訪れた
    visited[v] = 1
    if depth == 2:
        return
    for a, b in sides:
        if v == a-1:
            depth += 1
            dfs(b-1, depth)
            depth -= 1

n, m = MI()
sides = [LI() for _ in range(m)]
islands = [[0] * 2 for _ in range(n)]

for a, b in sides:
    if a-1 == 0:
        islands[b-1][0] = 1
    if b-1 == n-1:
        islands[a-1][1] = 1

for a, b in islands:
    if a == b == 1:
        print('POSSIBLE')
        exit()
print('IMPOSSIBLE')
