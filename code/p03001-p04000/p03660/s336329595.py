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
    F = [set() for _ in range(N)]
    for _ in range(N - 1):
        a, b = read_index()
        F[a].add(b)
        F[b].add(a)

    D = [0] * N
    S = deque()
    S.append((1, 0))
    S.append((-1, N - 1))
    D[0] = 1
    D[N - 1] = -1
    while S:
        c, p = S.popleft()
        for q in F[p]:
            if D[q] != 0:
                continue
            D[q] = c
            S.append((c, q))
    a = D.count(1)
    b = N - a
    print("Fennec" if a > b else "Snuke")
        

if __name__ == "__main__":
    main()
