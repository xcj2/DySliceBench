import bisect
import copy
import heapq
import sys
import itertools
import math
import queue
from functools import lru_cache
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
mod = 998244353

def read_values(): return map(int, input().split())
def read_index(): return map(lambda x: int(x) - 1, input().split())
def read_list(): return list(read_values())
def read_lists(N): return [read_list() for n in range(N)]


def to_char(a):
    return chr(a + ord("a"))

def main():
    N = int(input()) - 1

    res = ""
    while N >= 26:
        res = to_char(N % 26) + res
        N //= 26
        N -= 1

    print(to_char(N) + res)


if __name__ == "__main__":
    main()

