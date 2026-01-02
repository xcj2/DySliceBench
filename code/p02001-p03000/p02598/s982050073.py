import math
from functools import reduce
from collections import deque
from heapq import heappop, heappush
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

    n,k,*A = get_all_int()

    # NGの上限
    l = 0
    # OKの下限
    r = 10**9

    while l+1 < r:
        c = (l+r)//2

        # 全ての丸太を長さc以下にするのに何回かかるか？
        x = 0
        for a in A:
            # 切り上げ-1
            x += (a+c-1)//c - 1
        
        # log(l, r, c, x)

        if x <= k:
            # OK
            r = c
        else:
            # NG
            l = c

    print(r)

main()