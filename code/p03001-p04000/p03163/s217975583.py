import sys


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


INF = float('inf')


n, w = LI()
wv = LIR(n)
weight = [wv[i][0] for i in range(n)]
value = [wv[i][1] for i in range(n)]
# dp[i][j] : 重さ制限 j 、品物 i までを選べる状態での価値の最大値
dp = [[0] * (w + 1) for _ in range(n + 1)]
for i in range(n):
    for j in range(w + 1):
        if j - weight[i] >= 0:  # 品物 i が選べるかどうか
            dp[i + 1][j] = max(
                dp[i][j],  # 選ばない
                dp[i][j - weight[i]] + value[i]  # 選ぶ
            )
        else:
            dp[i + 1][j] = dp[i][j]
print(dp[n][w])
