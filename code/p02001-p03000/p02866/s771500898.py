import sys
stdin = sys.stdin

sys.setrecursionlimit(10 ** 7)

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x) - 1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

from collections import Counter

n = ni()
d = list(li())

mod = 998244353
dcnt = Counter(d)

# 正常か判断
def judge(n, d, dcnt):
    # 頂点1が0でないならNG
    for i in range(n):
        if i == 0 and d[i] != 0:
            return False
        if i > 0 and d[i] == 0:
            return False

    # keyが連続でなければNG
    dcnt_keys = sorted(list((dcnt.keys())))
    for i in range(len(dcnt_keys) - 1):
        if dcnt_keys[i+1] - dcnt_keys[i] != 1:
            return False

    return True

# dp
def dp(dcnt, mod):
    maxdepth = max(dcnt.keys())
    dp = [0]*(maxdepth+1)
    dp[0] = 1
    for depth in range(1, maxdepth+1):
        dp[depth] = dp[depth-1] * pow(dcnt[depth-1], dcnt[depth], mod)
        dp[depth] %= mod

    return dp[maxdepth]

if judge(n, d, dcnt):
    print(dp(dcnt, mod))
else:
    print(0)