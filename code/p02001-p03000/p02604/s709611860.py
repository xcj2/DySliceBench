import bisect
import copy
import heapq
import sys
import itertools
import math
from functools import lru_cache
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
mod = 10 ** 9 + 7 

def read_values(): return map(int, input().split())
def read_index(): return map(lambda x: int(x) - 1, input().split())
def read_list(): return list(read_values())
def read_lists(N): return [read_list() for n in range(N)]


def main():
    N = int(input())
    P = read_lists(N)
    # N = 15
    # P = [(i ** 2 + 1, i ** 2 + 1, i ** 2 + 1) for i in range(N)]
    
    C = [1 << 62] * (N + 1)
    # CX = [None for _ in range(2 ** N)]
    # CY = [None for _ in range(2 ** N)]
    CX = [1 << 62] * (N * 2 ** N)
    CY = [1 << 62] * (N * 2 ** N)

    LX = [0] * (2 ** N)
    LY = [0] * (2 ** N)
    for K in range(2 ** N):
        X = {0}
        Y = {0}
        for i in range(N):
            if (K >> i) & 1:
                X.add(P[i][0])
                Y.add(P[i][1])
         
        # CXX = [0] * N
        # CYY = [0] * N
        for j, (xp, yp, cp) in enumerate(P):
            for x in X:
                # CXX[j] = min(abs(xp - x) * cp, CXX[j])
                CX[K * N + j] = min(abs(xp - x) * cp, CX[K * N + j])
            for y in Y:
                CY[K * N + j] = min(abs(yp - y) * cp, CY[K * N + j])
                # CYY[j] = min(abs(yp - y) * cp, CYY[j])
            
        LX[K] = len(X)
        LY[K] = len(Y)
        # CX[K] = tuple(CXX)
        # CY[K] = tuple(CYY)

    for T in range(2 ** N):
        p = format(T, "160b").count("1")
        if C[p] == 0:
            continue

        r = 1 << 62
        tx = T
        while True:
            ty = T - tx
            c = 0
            for n in range(N):
                c += min(CX[tx * N + n], CY[ty * N + n])
            r = min(r, c)
            if tx == 0:
                break
            tx = (tx - 1) & T
        C[p] = min(C[p], r)
    print("\n".join(map(str, C)))


if __name__ == "__main__":
    main()
