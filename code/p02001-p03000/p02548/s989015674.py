import bisect
from collections import deque
import copy
import heapq
import sys
import itertools
import math
import queue
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
# mod = 10 ** 9 + 7
mod = 998244353

def read_values(): return map(int, input().split())
def read_index(): return map(lambda x: int(x) - 1, input().split())
def read_list(): return list(read_values())
def read_lists(N): return [read_list() for n in range(N)]



def main():
    N = int(input())
    res = 0
    for a in range(1, N):
        for b in range(1, N // a + 1):
            if a * b == N:
                continue
            res += 1

    print(res)

if __name__ == "__main__":
    main()