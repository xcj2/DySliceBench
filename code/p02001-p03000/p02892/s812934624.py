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


def f(S, i):
    D = [-1] * len(S)
    P = [set() for _ in range(len(S))]
    
    Q = deque()
    Q.append(i)
    D[i] = 1

    while Q:
        v = Q.popleft()

        for w in S[v]:
            if w in P[v]:
                continue
            
            if D[w] > 0 and D[w] < D[v] + 1:
                return -1

            if D[w] < 0:
                Q.append(w)
            P[w].add(v)
            D[w] = D[v] + 1

    return D[v]


def main():
    N = int(input())
    S = [input().strip() for _ in range(N)]
    L = [set(j for j in range(N) if S[i][j] == "1") for i in range(N)]

    res = -1
    for i in range(N):
        r = f(L, i)
        res = max(res, r) 
    
    print(res)


if __name__ == "__main__":
    main()
