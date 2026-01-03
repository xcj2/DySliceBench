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
    N, X = i_map()
    A = i_list()

    ans = [A[0]]
    cnt = 0

    for i,k in enumerate(A[1:]):
        t = k + ans[i]
        if t <= X:
            ans.append(k)
        else:
            if k - (t-X) >= 0:
                cnt += t - X
                ans.append(k - (t-X))
            else:
                cnt += t - X
                ans[-1] += k - (t-X)
                ans.append(0)
    print(cnt)











if __name__=="__main__":
    main()
