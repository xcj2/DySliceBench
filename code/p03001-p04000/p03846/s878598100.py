import math
from math import gcd,pi,sqrt
INF = float("inf")
MOD = 10**9 + 7

import sys
sys.setrecursionlimit(10**6)
import itertools
import bisect
from collections import Counter,deque
def i_input(): return int(input())
def i_map(): return map(int, input().split())
def i_list(): return list(i_map())
def i_row(N): return [i_input() for _ in range(N)]
def i_row_list(N): return [i_list() for _ in range(N)]
def s_input(): return input()
def s_map(): return input().split()
def s_list(): return list(s_map())
def s_row(N): return [s_input for _ in range(N)]
def s_row_str(N): return [s_list() for _ in range(N)]
def s_row_list(N): return [list(s_input()) for _ in range(N)]


def main():
    n = i_input()
    l = i_list()
    l.sort()

    if n == 1:
        if 0 in l:
            print(1)
            exit()
        else:
            print(0)
            exit()


    L = {}
    for i,k in itertools.groupby(l):
        L[i] = len(list(k))

    cnt = 0

    for i, k in L.items():
        if i == 0:
            if k > 1:
                print(0)
                exit()
        else:
            if k != 2:
                print(0)
                exit()
            else:
                cnt += 1
    print(2**cnt % MOD)









if __name__=="__main__":
    main()
