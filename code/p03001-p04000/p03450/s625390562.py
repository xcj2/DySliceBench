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
    N, M = read_values()
    F = [set() for _ in range(N)]
    T = set(i for i in range(N))
    for _ in range(M):
        L, R, D = read_values()
        L -= 1
        R -= 1
        F[L].add((R, D))
        T.discard(R)
    C = [-1] * N
    for t in T:
        S = deque()
        S.append(t)
        C[t] = 0
        while S:
            p = S.popleft()
            for q, d in F[p]:
                if C[q] == -1:
                    S.append(q)
                    C[q] = C[p] + d
                    continue
                if C[p] + d != C[q]:
                    print("No")
                    return
    if C.count(-1) > 0:
        print("No")
    else:
        print("Yes")


if __name__ == "__main__":
    main()
