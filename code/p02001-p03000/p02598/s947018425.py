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
    N, K = read_values()
    A = read_list()

    D = {}
    L = []

    l = 1
    r = max(A) + 1

    while l != r:
        m = (l + r) // 2 
        k = 0

        for a in A:
            k += (a - 1) // m 
        if k > K:
            l = m + 1
        else:
            r = m

    print(r)


if __name__ == "__main__":
    main()
