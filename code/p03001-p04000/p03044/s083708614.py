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


def f(N):
    res = 0
    while N != 0:
        b = format(N, "b").count("1")
        N %= b
        res += 1
    return res


def main():
    N = int(input())
    F = [[] for _ in range(N)]

    for _ in range(N - 1):
        u, v, w = read_values()
        u -= 1
        v -= 1
        F[u].append((v, w % 2))
        F[v].append((u, w % 2))

    D = [0] * N
    stack = [(0, 0, -1)]

    while stack:
        a, d, p = stack.pop()
        D[a] = d % 2

        for b, w in F[a]:
            if b == p:
                continue
            stack.append((b, (d + w) % 2, a))
    
    for d in D:
        print(d)


if __name__ == "__main__":
    main()
