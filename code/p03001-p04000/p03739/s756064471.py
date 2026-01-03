from collections import Counter
from functools import reduce
# import statistics
import bisect
import copy
import fractions
import math
import pprint
# for debug
pp = pprint.PrettyPrinter(width = 150)
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


n, a = II(), LI()
ruisekiwa = [0] * (n)
# 累積和の配列の最初の要素は、元のリストの最初の要素にする
ruisekiwa[0] = a[0]
for i in range(1, n):
    ruisekiwa[i] = ruisekiwa[i-1] + a[i]

ans1 = 0
ans2 = 0
diff = 0

# 偶数番目を正にする
for i in range(n):
    # 偶数番目なのに累積和が負
    # ruisekiwa[0] == -1 ならば1にするために2を加算する
    if i % 2 == 0 and ruisekiwa[i] + diff <= 0:
        ans1 += abs(1 - (ruisekiwa[i] + diff))
        diff += (1 - (ruisekiwa[i] + diff))
        # print(ans1, diff)
    # 奇数番目なのに累積和が正
    elif i % 2 == 1 and ruisekiwa[i] + diff >= 0:
        ans1 += abs(ruisekiwa[i] + diff - (-1))
        diff += ((-1) - (ruisekiwa[i] + diff))
        # print(ans1, diff)
        
diff = 0
# 偶数番目を負にする
for i in range(n):
    # 偶数番目なのに累積和が正
    if i % 2 == 0 and ruisekiwa[i] + diff >= 0:
        # -1にするためにどれだけ減算するか
        ans2 += abs(ruisekiwa[i] + diff - (-1))
        diff += ((-1) - (ruisekiwa[i] + diff))
        # print(ans2, diff)
    # 奇数番目なのに累積和が負
    elif i % 2 == 1 and ruisekiwa[i] + diff <= 0:
        ans2 += abs(1 - (ruisekiwa[i] + diff))
        diff += (1 - (ruisekiwa[i] + diff))
        # print(ans2, diff)
        
print(min(ans1, ans2))
