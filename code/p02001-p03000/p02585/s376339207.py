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


class V:
    def __init__(self, f, v=None):
        self.f = f
        self.v = v
 
    def __str__(self):
        return str(self.v)
 
    def ud(self, n):
        if n is None:
            return

        if self.v is None:
            self.v = n
            return
        self.v = self.f(self.v, n) 


def main():
    N, K = read_values()
    P = read_list()
    C = read_list()

    res = V(max)
    for i in range(N):
        t = []
        c = 0
        p = i
        while len(t) == 0 or p != i:
            p = P[p] - 1
            c += C[p]
            t.append(c)

        m = len(t)
        # print(f"m: {m}, t: {t}, c: {c}")
        if m > K or c <= 0:
            res.ud(max(t[:K]))
        else:
            s = K // m * c
            k = K % m
            # print(f"s: {s}, k: {k}")
            tmp = V(max)
            for i in range(k):
                tmp.ud(s + t[i])
            
            s -= c
            for v in t:
                tmp.ud(s + v)
            
            res.ud(tmp.v)

    print(res)


if __name__ == "__main__":
    main()

