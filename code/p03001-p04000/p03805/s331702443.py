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
    global L
    N,m = i_map()
    l = [[0]*N for i in range(N)]

    for i in range(m):
        a,b = i_map()
        a -= 1
        b -= 1
        l[a][b] = 1
        l[b][a] = 1

    L = 0
    v = [0] * N
    v[0] = 1

    def dfs(n):
        global L
        if 0 not in v:
            L += 1
            return

        for i in range(N):
            if l[n][i] == 1 and v[i] == 0:
                v[i] = 1
                dfs(i)
                v[i] = 0

    dfs(0)
    print(L)



if __name__=="__main__":
    main()
