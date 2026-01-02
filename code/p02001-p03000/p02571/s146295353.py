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
    S = input().strip()
    T = input().strip()

    res = len(T)
    for i in range(len(S) - len(T) + 1):
        res = min(res, sum(1 if s != t else 0 for s, t in zip(S[i:], T)))

    print(res)

if __name__ == "__main__":
    main()

