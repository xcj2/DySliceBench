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
    n = i_input()
    v = i_list()

    fd = {}
    sd = {}
    for i,k in enumerate(v):
        if i%2==0:
            fd[k] = fd.get(k,0) + 1
        else:
            sd[k] = sd.get(k,0) + 1

    a = max(fd, key=fd.get)
    b = max(sd, key=sd.get)
    c = max(fd.values())
    d = max(sd.values())

    if a != b:
        print(n - c - d)
    else:
        fd[a] = 0
        sd[b] = 0
        e = max(fd.values())
        f = max(sd.values())
        z = max(c+f , d+e)
        print(n-z)


if __name__=="__main__":
    main()
