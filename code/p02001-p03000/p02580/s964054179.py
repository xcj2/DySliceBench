import math
from functools import reduce
from collections import deque
import sys
sys.setrecursionlimit(10**7)
from bisect import bisect_left
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

    h,w,m = get_nums_l()
    targets = []
    H = []
    W = []
    HW = []
    for i in range(m):
        hi, wi = get_nums_l()
        HW.append((hi-1, wi-1))
        H.append(hi-1)
        W.append(wi-1)

    HW.sort()
    
    rows = [0] * h
    cols = [0] * w

    for i in range(m):
        rows[H[i]] += 1
        cols[W[i]] += 1

    rmax = 0
    rmaxi = []
    for i,x in enumerate(rows):
        if x > rmax:
            rmax = x
            rmaxi = [i]
        elif x == rmax:
            rmaxi.append(i)
    cmax = 0
    cmaxi = []
    for i,x in enumerate(cols):
        if x > cmax:
            cmax = x
            cmaxi = [i]
        elif x == cmax:
            cmaxi.append(i)

    # log(rmax,cmax)
    # log(rmaxi, cmaxi)

    for rmi in rmaxi:
        for cmi in cmaxi:
            ok = True
            i = bisect_left(HW, (rmi, cmi))
            if i<m and HW[i] == (rmi, cmi):
                ok = False
            # for i in range(m):
            #     if H[i] == rmi and W[i] == cmi:
            #         ok = False
            #         break
            if ok:
                print(rmax + cmax)
                return

    print(rmax + cmax - 1)

main()