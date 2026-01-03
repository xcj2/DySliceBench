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
    a = i_list()
    dic = {399:0, 799:0, 1199:0, 1599:0, 1999:0, 2399:0, 2799:0, 3199:0}
    cnt = 0
    for i in a:
        if i < 400:
            dic[399] = 1
        elif i < 800:
            dic[799] = 1
        elif i < 1200:
            dic[1199] = 1
        elif i < 1600:
            dic[1599] = 1
        elif i < 2000:
            dic[1999] = 1
        elif i < 2400:
            dic[2399] = 1
        elif i < 2800:
            dic[2799] = 1
        elif i < 3200:
            dic[3199] = 1
        else:
            cnt += 1
    c = sum(list(dic.values()))
    if c == 0:
        print(1, cnt)
    else:
        print(c, c+cnt)





if __name__=="__main__":
    main()
