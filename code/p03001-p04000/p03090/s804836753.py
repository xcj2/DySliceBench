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

    M = N * (N - 1) // 2 - N // 2
    print(M)
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            if i + j == 1 + N - N % 2:
                continue
            print(i, j)


if __name__ == "__main__":
    main()