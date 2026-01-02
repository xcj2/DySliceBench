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

import string

def main():
    n = i_input()
    dic = {"M":0,"A":0,"R":0,"C":0,"H":0}
    key = list(dic.keys())
    for _ in range(n):
        i = s_input()
        t = i[0]
        if t in key:
            dic[t] = dic.get(t) + 1
    ans = 0
    check = False
    l = list(dic.values())
    l = list(itertools.combinations(l, 3))
    for i in l:
        a = i[0]
        b = i[1]
        c = i[2]
        if a != 0 and b != 0 and c != 0:
            ans += a*b*c
            check = True
    if check:
        print(ans)
    else:
        print(0)


if __name__=="__main__":
    main()
