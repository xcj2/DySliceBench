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
    N, M = read_values()
    L = [set() for _ in range(N)]
    for _ in range(M):
        a, b = read_index()
        L[a].add(b)
        L[b].add(a)

    res = 0
    for T in itertools.permutations(range(1, N)):
        pre = 0
        for t in T:
            if t not in L[pre]:
                break
            pre = t
        else:
            res += 1

    print(res)


if __name__ == "__main__":
    main()

