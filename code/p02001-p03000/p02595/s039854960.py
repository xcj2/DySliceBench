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
    N, D = read_values()
    D *= D
    res = 0
    for _ in range(N):
        X, Y = read_values()
        if X ** 2 + Y ** 2 <= D:
            res += 1
    print(res)

if __name__ == "__main__":
    main()
