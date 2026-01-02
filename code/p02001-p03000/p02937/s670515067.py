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
    T = input().strip()

    D = {chr(i): [] for i in range(ord("a"), ord("z") + 1)}

    for i, s in enumerate(S):
        D[s].append(i)
    
    res = 0
    p = 0
    for t in T:
        if D[t] == []:
            print(-1)
            return
        
        j = bisect.bisect_left(D[t], p)
        if j == len(D[t]):
            p = D[t][0] + 1
            res += 1
        else:
            p = D[t][j] + 1
        
    print(res * len(S) + p)


if __name__ == "__main__":
    main()

