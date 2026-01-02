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
    l = [[0]*10 for i in range(10)]
    for i in range(1,n+1):
        s = str(i)
        head = int(s[0])
        tail = int(s[-1])
        l[head][tail] += 1
    ans = 0

    for i in range(1,10):
        for j in range(i,10):
            if i == j:
                ans += l[i][j]**2
            else:
                one = l[i][j]
                two = l[j][i]
                ans += one*two*2
    print(ans)



if __name__=="__main__":
    main()
