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
    a = list(s_input())
    b = list(s_input())
    c = list(s_input())

    t = "a"

    while True:
        if t == "a":
            if len(a) == 0:
                print("A")
                exit()

            t = a.pop(0)
        elif t == "b":
            if len(b) == 0:
                print("B")
                exit()

            t = b.pop(0)
        else:
            if len(c) == 0:
                print("C")
                exit()
            t = c.pop(0)


if __name__=="__main__":
    main()
