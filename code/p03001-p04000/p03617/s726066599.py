# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline
def ii(): return int(input())
def mi(): return map(int, input().rstrip().split())
def lmi(): return list(map(int, input().rstrip().split()))
def fi(): return float(input())
def mfi(): return map(float, input().rstrip().split())
def lmfi(): return list(map(float, input().rstrip().split()))
def li(): return list(input().rstrip())
def debug(*args, sep=" ", end="\n"): print("debug:", *args, file=sys.stderr, sep=sep, end=end) if not __debug__ else None
def exit(*arg): print(*arg); sys.exit()
# template


def main():
    Q, H, S, D = mi()
    N = ii()
    N *= 4
    dp = [10**10] * 9
    dp[0] = 0
    for i in range(1, 9):
        dp[i] = min(dp[i - 1] + Q, dp[i])
    for i in range(2, 9):
        dp[i] = min(dp[i - 2] + H, dp[i])
    for i in range(4, 9):
        dp[i] = min(dp[i - 4] + S, dp[i])
    for i in range(8, 9):
        dp[i] = min(dp[i - 8] + D, dp[i])
    # print(dp)
    m = min(8 * Q, 4 * H, 2 * S, D)
    print(m * (N // 8) + dp[N % 8])
    return


if __name__ == '__main__':
    main()
