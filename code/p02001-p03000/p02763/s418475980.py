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


def _get(T, a, b, k, l, r):
    if r <= a or b <= l:
        return set()

    if a <= l and r <= b:
        return T[k]
    else:
        s1 = _get(T, a, b, 2 * k + 1, l, (l + r) // 2)
        s2 = _get(T, a, b, 2 * k + 2, (l + r) // 2, r)
        return s1.union(s2)


def get(T, d, a, b):
    return _get(T, a, b, 0, 0, 2 ** d)


def main():
    N = int(input())
    S = input().strip()
    Q = [input().strip().split() for _ in range(int(input()))]
    d = N.bit_length()
    T = [set() for _ in range(2 ** (d + 1) - 1)]
    for i, s in enumerate(S):
        T[i + 2 ** d - 1].add(s)
    for i in range(2 ** d - 2, -1, -1):
        T[i] =T[2 * i + 1] .union(T[2 * i + 2])

    for s, a, b in Q:
        if s == "1":
            a = int(a) - 1
            i = a + 2 ** d - 1
            if b in T[i]:
                continue
            T[i] = {b}
            while i > 0:
                i = (i - 1) // 2
                T[i] = T[2 * i + 1] .union(T[2 * i + 2])
        elif s == "2":
            a = int(a) - 1
            b = int(b) - 1
            S = get(T, d, a, b + 1)
            print(len(S))


if __name__ == "__main__":
    main()
