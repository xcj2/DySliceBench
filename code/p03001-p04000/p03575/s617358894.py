from collections import Counter
from functools import reduce
# import statistics
import bisect
import copy
import fractions
import math
import random
import pprint
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


# nは頂点の数
n, m = MI()
ans = 0
sides = [LI() for _ in range(m)]
# 隣接行列を用いてグラフの管理をする
# graph = [[False] * n for _ in range(n)]

# もしグラフ全体が連結ならばuf[i]=iとなる頂点がただ1つだけある
# Union-Find
for i in range(m):

    # 最初各ノードの根は自分自身
    node = [k for k in range(n)]
    
    for j, side in enumerate(sides):
        
        # 連結しない
        if i == j:
            continue

        unite(side[0]-1, side[1]-1)

    # 根が自分自身であるものが2つ以上存在する場合、グラフは非連結である
    # 1である場合連結なのでのぞいた辺は橋「ではない」
    if sum(node[num] == num for num in range(len(node))) != 1:
        ans += 1

print(ans)
