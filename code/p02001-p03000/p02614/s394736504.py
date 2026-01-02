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

    h,w,k = get_nums_l()
    grid_s = [input() for _ in range(h)]

    ans = 0
    for by in range(2**h):
        for bx in range(2**w):
            c = 0

            for y in range(h):
                for x in range(w):
                    if 2**y & by == 0 and 2**x & bx == 0 and grid_s[y][x] == "#":
                        c += 1

            if c == k:
                ans += 1
    
    print(ans)


main()