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
    N, K = read_values()
    A = read_list()

    for k in range(K):
        S = [0] * (N + 1)
        for i, a in enumerate(A):
            S[max(0, i - a)] += 1
            S[min(N, i + a + 1)] -= 1
        
        A[-1] = 0
        c = 0
        for i, s in enumerate(S[:N]):
            A[i] = A[i - 1] + s
            if A[i] == N:
                c += 1
            
        if c == N:
            break

    print(" ".join(map(str, A)))


if __name__ == "__main__":
    main()

