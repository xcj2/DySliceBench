from collections import Counter
from functools import reduce
# import statistics
import bisect
import copy
import fractions
import math
import pprint
pp = pprint.PrettyPrinter(width = 300)
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


# dp
n = II()
s = [II() for i in range(n)]
tmp = 10010
dp = [[0 for i in range(tmp)] for j in range(n+1)]
dp[0][0] = 1
for i in range(n):
    for j in range(tmp):
        if s[i] <= j:
            dp[i+1][j] = dp[i][j-s[i]] or dp[i][j]
        else:
            dp[i+1][j] = dp[i][j]

ans = 0
for i, num in enumerate(dp[n]):
    if num == 1 and i % 10 != 0:
        ans = i
print(ans)
