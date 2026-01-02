import math
from functools import reduce
from collections import deque
from bisect import bisect_left
import sys
sys.setrecursionlimit(10**7)
# sys.stdin.readline

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [ int(s) for s in input().split(" ")]

# 改行区切りの入力をn行読み込んで数値リストにして返します。
def get_nums_n(n):
    return [ int(input()) for _ in range(n)]

# 改行またはスペース区切りの入力をすべて読み込んでイテレータを返します。
def get_all_int():
    return map(int, open(0).read().split())

def rangeI(it, l, r):
    for i, e in enumerate(it):
        if l <= i < r:
            yield e
        elif l >= r:
            break

def log(*args):
    print("DEBUG:", *args, file=sys.stderr)

INF = 999999999999999999999999
MOD = 10**9+7

n = int(input())
A = [-INF] + get_nums_l()
edges = [ [] for _ in range(n+1) ]
for line in map(lambda s: s.strip(), sys.stdin.readlines()):
    u,v = map(int, line.split())
    edges[u].append(v)
    edges[v].append(u)

def dfs(dp, u, p=None):

    # log(u)
    # log(dp)

    # dpの中でA[u]以上の値が入っている最小のindex
    i = bisect_left(dp, A[u])

    old = dp[i]
    dp[i] = A[u]

    # 有効値(INF以外)が入っている最大のindex
    ans[u] = bisect_left(dp, INF) - 1

    for v in edges[u]:
        if v == p:
            continue
        dfs(dp, v, u)

    # 巻き戻し
    dp[i] = old

# ans[i] = ノード1からノードiへの経路中の最長増加部分列長
ans = [0] * (n+1)

# dp[i] = 最長増加部分列長がiの場合の末尾ノード値の最小
dp = [INF] * (n+1)
dp[0] = -INF
dfs(dp, 1, None)

for i in range(1, n+1):
    print(ans[i])
