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
    MOD = 10**9+7

    n,m,k = get_nums_l()
    A = get_nums_l()
    B = get_nums_l()

    ruisekiA = [0] * (n+1)
    ruisekiB = [0] * (m+1)
    for i in range(n):
        ruisekiA[i+1] = ruisekiA[i] + A[i]
    for i in range(m):
        ruisekiB[i+1] = ruisekiB[i] + B[i]

    ans = 0

    # i = Aの本を読む冊数
    for i in range(n+1):

        if ruisekiA[i] > k:
            # Aだけでk分をオーバーしていたらNG
            continue

        # Bの本を読める冊数を二分探索で求める
        # OKの下限
        l = 0
        # NGの下限
        r = m+1

        while l+1 < r:
            c = (l+r) // 2

            # log(i,c)
            if ruisekiA[i] + ruisekiB[c] <= k:
                l = c
            else:
                r = c
        
        ans = max(ans, i+l)

    print(ans)

main()