import sys
from collections import deque
from functools import lru_cache
import bisect
import copy
import heapq
import itertools
import math
import random
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
mod = 10 ** 9 + 7

def read_values(): return map(int, input().split())
def read_index(): return map(lambda x: int(x) - 1, input().split())
def read_list(): return list(read_values())
def read_lists(N): return [read_list() for n in range(N)]


def main():
    N, A, B = read_values()
    V = [int(input()) for _ in range(N)]
    K = A - B
    l = 0
    r = max((v - 1) // B + 1 for v in V)
    while l < r - 1:
        m = (l + r) // 2

        t = 0
        for v in V:
            u = v - m * B
            t += max(0, (u + K - 1) // K)
        
        if t > m:
            l = m
        else:
            r = m
    
    print(r)


if __name__ == "__main__":
    main()

