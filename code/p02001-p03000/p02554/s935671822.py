import sys
from collections import deque
from functools import lru_cache
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
    if N == 1:
        print(0)
        return

    res = pow(10, N, mod)
    res -= 2 * pow(9, N, mod)
    res %= mod
    res += pow(8, N, mod)
    res %= mod
    print(res)


if __name__ == "__main__":
    main()

