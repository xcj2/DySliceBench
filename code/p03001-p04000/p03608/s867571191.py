import math
from math import gcd,pi,sqrt
INF = float("inf")

import sys
sys.setrecursionlimit(10**6)
import itertools
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
    n,m,R = i_map()
    r = i_list()
    c = [[INF]*n for i in range(n)]
    for i in range(n):
        c[i][i] = 0

    for _ in range(m):
        a,b,d = i_map()
        a -= 1
        b -= 1
        c[a][b] = c[b][a] = d

    for k in range(n): # 経由
        for i in range(n): # 始点
            for j in range(n): # 終点
                c[i][j] = min(c[i][j], c[i][k] + c[k][j])

    r = list(itertools.permutations(r, R))

    ans = INF
    for i in r:
        trial = 0
        for k in range(len(i)-1):
            a = i[k] - 1
            b = i[k+1] - 1
            trial += c[a][b]
        ans = min(ans,trial)
    print(ans)




if __name__=="__main__":
    main()
