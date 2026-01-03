import sys
from collections import deque
import bisect
import copy
import heapq
import itertools
import math
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
mod = 10 ** 9 + 7

def read_values(): return map(int, input().split())
def read_index(): return map(lambda x: int(x) - 1, input().split())
def read_list(): return list(read_values())
def read_lists(N): return [read_list() for n in range(N)]


def main():
    N = int(input())
    A = read_list()
    res = 10 ** 20
    
    for i in range(2):
        tmp = 0
        t = 0
        s = (-1) ** i
        for a in A:
            t += a
            if  t * s >= 0:
                tmp += abs(t) + 1
                t = -s
            s = -s
        res = min(res, tmp)
    print(res)


if __name__ == "__main__":
    main()
