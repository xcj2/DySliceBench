from collections import Counter
from collections import deque
from functools import reduce
from pprint import pprint
# import statistics
import bisect
import copy
import fractions
import math
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
s = [IS() for _ in range(n)]
cnt = 0
sentou_b = 0
ushiro_a = 0
ab = 0
for i in s:
    cnt += i.count('AB')
    if i[0] == 'B' and i[-1] == 'A':
        ab += 1
    else:
        if i[0] == 'B':
            sentou_b += 1
        if i[-1] == 'A':
            ushiro_a += 1
if ab == 0:
    print(cnt+min(sentou_b, ushiro_a))
elif ab > 0:
    if sentou_b + ushiro_a > 0:
        print(cnt+ab+min(sentou_b, ushiro_a))
    elif sentou_b + ushiro_a == 0:
        print(cnt+ab-1)
