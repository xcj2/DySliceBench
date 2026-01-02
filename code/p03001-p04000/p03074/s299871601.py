import math
from math import gcd,pi,sqrt
INF = float("inf")
MOD = 10**9 + 7

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
    n,K = i_map()
    s = list(input())

    l = []
    if s[0] == "0":
        l.append(0)

    for i,k in itertools.groupby(s):
        l.append(len(list(k)))
    if s[-1] == "0":
        l.append(0)

    l = list(itertools.accumulate(l))

    ans = 0
    if len(l) < 2*K:
        ans = max(l)
        print(ans)
        exit()

    for i in range(0,n,2):
        if i+2*K >= len(l):
            break
        if i == 0:
            ans = max(ans, l[(i+2*K)])
        else:
            ans = max(ans, l[(i+2*K)] - l[i-1])
    print(ans)






if __name__=="__main__":
    main()
