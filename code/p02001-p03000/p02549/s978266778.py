import math
from functools import reduce
from collections import deque
import sys
sys.setrecursionlimit(10**7)

def input():
    return sys.stdin.readline().strip()

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [ int(s) for s in input().split(" ")]

# 改行またはスペース区切りの入力をすべて読み込んでイテレータを返します。
def get_all_int():
    return map(int, open(0).read().split())

def log(*args):
    print("DEBUG:", *args, file=sys.stderr)

def main():
    INF = 999999999999999999999999
    MOD = 998244353

    n,k = get_nums_l()

    steps = []
    for _ in range(k):
        l,r = get_nums_l()
        steps.append((l,r))
    
    # log(steps)

    # dp[i] = iマスまで行く方法のパターン数
    dp = [0] * (n)
    ruiseki = [0] * (n+1)

    dp[0] = 1
    ruiseki[1] = 1

    for i in range(1, n):
        for a,b in steps:
            l = max(0, i-b)
            r = i-a
            # log("A", i,l,r)
            if r < 0:
                continue

            add = (ruiseki[r+1] - ruiseki[l])
            dp[i] = (dp[i] + add) % MOD
            # log("  B", add)
        ruiseki[i+1] = (ruiseki[i] + dp[i]) % MOD
        # log(dp, ruiseki)

    print(dp[n-1] % MOD)

main()