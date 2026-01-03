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


H, W = MI()
mini_a = INF
mini_b = INF
mini1 = INF
mini2 = INF
mini3 = INF
mini4 = INF
for h in range(1,H):
    sa = h * W
    sb = (H-h) * math.floor(W/2)
    sc = (H-h) * (W - math.floor(W/2))
    sd = (math.floor((H-h)/2)) * W
    se = (H-h-math.floor((H-h)/2)) * W
    mini1 = min(mini1, max(sa,max(sb,sc)) - min(sa,min(sb,sc)))
    mini2 = min(mini2, max(sa,max(sd,se)) - min(sa,min(sd,se)))
    mini_a = min(mini1,mini2)
for w in range(1,W):
    sa = H * w
    sb = (W-w) * math.floor(H/2)
    sc = (W-w) * (H - math.floor(H/2))
    sd = (math.floor((W-w)/2)) * H
    se = (W-w-math.floor((W-w)/2)) * H
    mini3 = min(mini3, max(sa,max(sb,sc)) - min(sa,min(sb,sc)))
    mini4 = min(mini4, max(sa,max(sd,se)) - min(sa,min(sd,se)))
    mini_b = min(mini3,mini4)
print(min(mini_a,mini_b))
