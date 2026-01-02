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
visited = [False] * n
# 隣接行列を用いてグラフの管理をする
graph = [[False] * n for _ in range(n)]

# 初期化、graph[i-1][j-1] = 1ならば頂点i,jは連結している
for a, b in sides:
    graph[a-1][b-1] = True
    graph[b-1][a-1] = True 

# pprint.pprint(graph)

for a, b in sides:
    # 辺の削除
    graph[a-1][b-1] = False
    graph[b-1][a-1] = False

    for i in range(n):
        visited[i] = False
    
    dfs(0)

    # 探索実行後訪れていないノードが1つでもあれば
    # 削除した辺は橋である
    for i in range(n):
        if visited[i] == False:
            ans += 1
            break

    # 辺を元に戻す
    graph[a-1][b-1] = True
    graph[b-1][a-1] = True

print(ans)
