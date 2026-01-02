import numpy as np
import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def main():
    md = 998244353
    n = int(input())
    mx = 90005
    dp = np.zeros(mx, dtype="i8")
    dp2 = np.zeros(mx, dtype="i8")
    dp[0] = 1
    dp2[0] = 1
    sum_a = 0
    for _ in range(n):
        a = int(input())
        sum_a += a
        dp[mx - 1:a - 1:-1] = dp[mx - 1:a - 1:-1] * 2 + dp[mx - a - 1::-1]
        dp[:a] *= 2
        dp %= md
        dp2[mx - 1:a - 1:-1] += dp2[mx - a - 1::-1]
        dp2 %= md
    ng = np.sum(dp[(sum_a + 1) // 2:]) - np.sum(dp2[(sum_a + 1) // 2:]) * 2 + 1
    ng %= md
    total = (pow(3, n, md) - 3 * pow(2, n, md) + 3) % md
    print((total - ng * 3) % md)
    # ALL-NG（NG…最大辺が周の半分以上になる）で求める
    # 最大辺を赤として、dp[r] 赤の和がrのパターンを求める
    # 「赤だけ」、「赤と他一色だけ」(両方dp2に含まれる)のパターンは除く必要がある
    # 赤の和が総和の半分以上になるパターンを考えるので、
    # 赤以外の色だけになるパターンは除く必要がない
    # その後、緑、青が最大の辺になる場合も考えて3倍

main()
