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
    N, u, v = read_values()
    u -= 1
    v -= 1
    F = [set() for _ in range(N)]
    for _ in range(N - 1):
        a, b = read_index()
        F[a].add(b)
        F[b].add(a)

    D = [-1] * N
    S = deque()
    S.append((0, v))
    D[v] = 0
    while S:
        c, p = S.popleft()
        for q in F[p]:
            if D[q] != -1:
                continue
            D[q] = c + 1
            S.append((c + 1, q))

    E = [-1] * N
    S.append((0, u))
    E[u] = 0
    while S:
        c, p = S.popleft()
        for q in F[p]:
            if E[q] != -1  or D[q] < c + 1:
                continue
            E[q] = c + 1
            S.append((c + 1, q))
    
    res = 0
    for i in range(N):
        if E[i] < 0:
            continue
        res = max(res, D[i])
    print(res - 1)


if __name__ == "__main__":
    main()
