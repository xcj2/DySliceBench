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
    a,b,c,d,e,f = i_map()
    W = set()
    for i in range(0,f+1,a*100):
        for j in range(0,f+1, b*100):
            W.add(i+j)

    S = set()
    for i in range(0,f+1, c):
        for j in range(0, f+1, d):
            S.add(i+j)

    rate = -1

    for w in W:
        for s in S:
            if 0 < w+s <= f and s <= w*e//100:
                if s/(w+s) > rate:
                    rate = s/(w+s)
                    ans = (w+s,s)
    print(ans[0], ans[1])





if __name__=="__main__":
    main()
