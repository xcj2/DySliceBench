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
mod = 10 ** 9 + 7 

def read_values(): return map(int, input().split())
def read_index(): return map(lambda x: int(x) - 1, input().split())
def read_list(): return list(read_values())
def read_lists(N): return [read_list() for n in range(N)]


def main():
    S = input().strip()

    res = 0
    for i, s in enumerate(S):
        if s == "g":
            res += i % 2
        elif s == "p":
            res -= (i + 1) % 2
    print(res)



if __name__ == "__main__":
    main()
