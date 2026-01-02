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
    K = int(input())
    a = 7
    a %= K
    for k in range(K):
        if a % K == 0:
            print(k + 1)
            return
        a = a * 10 + 7
        a %= K
    print(-1)


if __name__ == "__main__":
    main()
