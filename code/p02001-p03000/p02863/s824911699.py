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

from collections import defaultdict

n, t = li()
ab = [tuple(li()) for _ in range(n)]
ans = 0

# dp
dp = [[0]*t for _ in range(n+1)]

for i, (ai, bi) in enumerate(ab):
    for ti in range(t):
        if ti + ai < t:
            dp[i+1][ti + ai] = max(dp[i][ti + ai], dp[i][ti] + bi)
        dp[i+1][ti] = max(dp[i+1][ti], dp[i][ti])

# 経路復元
chose = set()
maxtime = dp[n].index(max(dp[n]))

for idx in range(n, 0, -1):
    if dp[idx][maxtime] != dp[idx-1][maxtime]:
        chose.add(idx-1)
        maxtime -= ab[idx-1][0]

allitem = set(range(n))
notchose = allitem - chose

notchosemax = 0
if notchose:
    for i in notchose:
        notchosemax = max(notchosemax, ab[i][1])

print(max(dp[n]) + notchosemax)
