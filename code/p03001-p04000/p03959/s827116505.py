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
    A = read_list()
    B = read_list()
    S = [10 ** 9] * N
    T = [1] * N

    r = 0
    for i ,a in enumerate(A):
        S[i] = min(S[i], a)
        if r < a:
            T[i] = max(T[i], a)
        r = a
    
    r = 0
    for j, b in enumerate(B[::-1]):
        i = N - 1 - j
        S[i] = min(S[i], b)
        if r < b:
            T[i] = max(T[i], b)
        r = b

    res = 1
    for s, t in zip(S, T):
        res *= max(0, s - t + 1)
        res %= mod
    print(res)


if __name__ == "__main__":
    main()
