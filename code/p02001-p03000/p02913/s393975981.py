import sys
from collections import deque
import bisect
import copy
import heapq
import itertools
import math
from typing import overload
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
mod = 10 ** 9 + 7

def read_values(): return map(int, input().split())
def read_index(): return map(lambda x: int(x) - 1, input().split())
def read_list(): return list(read_values())
def read_lists(N): return [read_list() for n in range(N)]


def z_algo(S):
    N = len(S)
    Z = [0] * N
    Z[0] = N

    i = 1
    j = 0
    while i < N:
        while i + j < N and S[j] == S[i + j]:
            j += 1
        Z[i] = j

        if j == 0:
            i += 1
            continue

        k = 1
        while k < j and k + Z[k] < j:
            Z[i + k] = Z[k]
            k += 1
        
        i += k
        j -= k
    return Z


def main():
    N = int(input())
    S = input().strip()

    res = 0
    for i in range(N - 1):
        Z = z_algo(S[i:])
        t = 0
        for i, z in enumerate(Z):
            if i < z:
                continue
            t = max(t, z)
        res = max(res, t)
        
    print(res)


if __name__ == "__main__":
    main()

