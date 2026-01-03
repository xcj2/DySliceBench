import bisect
import copy
import heapq
import sys
import itertools
import math
import queue
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
mod = 10 ** 9 + 7

def read_values(): return map(int, input().split())
def read_index(): return map(lambda x: int(x) - 1, input().split())
def read_list(): return list(read_values())
def read_lists(N): return [read_list() for n in range(N)]
def init_dp1(init, N): return [init for _ in range(N)]
def init_dp2(init, N, M): return [[init for _ in range(M)] for _ in range(N)]


def f(S, T):
    N = len(S)
    F = [[0 for _ in range(N)] for __ in range(N)]
    
    for i in range(N):
        for j in range(N):
            SS = S[i]
            TT = T[j]
            if TT == (0, 0):
                F[i][j] = 1 if SS == (0, 1) else 0
            elif TT == (0, 1):
                if SS == (1, 0):
                    return None
                F[i][j] = 1
            elif TT == (1, 0):
                if SS == (0, 1):
                    return None
                F[i][j] = 0
            else:
                F[i][j] = 0 if SS == (1, 0) else 1

    return F


def main():
    N, L = read_values()
    A = read_list()

    r = 0
    for i in range(N - 1):
        if A[i] + A[i + 1] >= L:
            r = i
            break
    else:
        print("Impossible")
        return

    print("Possible")
    
    for i in range(r):
        print(i + 1)
    for i in range(N - 2, r - 1, -1):
        print(i + 1)


if __name__ == "__main__":
    main()
