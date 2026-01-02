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
    L = [i_list() for i in range(n-1)]

    ans = []

    for l in range(n-1):
        time = L[l][1] + L[l][0]
        for j in range(n-l-2):
            t = l+j+1
            if time <= L[t][1]: # まだ出発していない
                time = L[t][1] + L[t][0]
            elif (time - L[t][1]) % L[t][2] == 0: # ちょうど出発タイミング
                time += L[t][0]
            else: # すでに出発はしていて、待ち時間発生
                s = (time - L[t][1])//L[t][2] + 1
                time = L[t][1] + L[t][2]*s + L[t][0]
        print(time)
    print(0)




if __name__=="__main__":
    main()
