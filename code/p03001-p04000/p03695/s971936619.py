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
def dfs(v):
    # ノードに訪れた
    visited[v] = True
    for v2 in range(n):
        if graph[v][v2] == False:  # そもそもvとv2が辺でつながっていない
            continue
        if visited[v2] == True:  # もう見た
            continue
        dfs(v2)


n = II()
a = LI()
colors = [0] * 9
for rate in a:
    if 1 <= rate <= 399:
        colors[0] += 1
    elif 400 <= rate <= 799:
        colors[1] += 1
    elif 800 <= rate <= 1199:
        colors[2] += 1
    elif 1200 <= rate <= 1599:
        colors[3] += 1
    elif 1600 <= rate <= 1999:
        colors[4] += 1
    elif 2000 <= rate <= 2399:
        colors[5] += 1
    elif 2400 <= rate <= 2799:
        colors[6] += 1
    elif 2800 <= rate <= 3199:
        colors[7] += 1
    else:
        colors[8] += 1
ans = sum(colors[i] >= 1 for i in range(8))
if ans != 0:
    print(str(ans) + ' ' + str(ans + colors[8]))
else:
    print(str('1') + ' ' + str(colors[8]))
