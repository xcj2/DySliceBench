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


def cal(A, F, m):
    res = 0
    for a, f in zip(A, F):
        c = m // f
        res += max(0, a - c)
    return res


def main():
    N, K = read_values()
    A = read_list()
    F = read_list()
    A.sort()
    F.sort(reverse=True)

    l = 0
    r = 10 ** 12
    while l < r:
        m = (l + r) // 2
        if cal(A, F, m) > K:
            l = m + 1
        else:
            r = m
    
    print(r)


if __name__ == "__main__":
    main()