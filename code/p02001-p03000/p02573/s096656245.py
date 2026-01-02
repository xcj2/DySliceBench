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


class UF:
    def __init__(self, N):
        self.state = [-1] * N
        self.rank = [0] * N
        self.num_group = N
    
    def get_parent(self, a):
        p = self.state[a]
        if p < 0:
            return a
        
        q = self.get_parent(p)
        self.state[a] = q
        return q

    def make_pair(self, a, b):
        pa = self.get_parent(a)
        pb = self.get_parent(b)
        if pa == pb:
            return

        if self.rank[pa] > self.rank[pb]:
            pa, pb = pb, pa
            a, b = b, a
        elif self.rank[pa] == self.rank[pb]:
            self.rank[pb] += 1

        self.state[pb] += self.state[pa]
        self.state[pa] = pb
        self.state[a] = pb
        self.num_group -= 1
    
    def is_pair(self, a, b):
        return self.get_parent(a) == self.get_parent(b)

    def get_size(self, a):
        return -self.state[self.get_parent(a)]


def main():
    N, M = read_values()
    uf = UF(N)
    for _ in range(M):
        A, B = read_index()
        uf.make_pair(A, B)

    res = 0
    for n in range(N):
        res = max(res, uf.get_size(n))

    print(res)


if __name__ == "__main__":
    main()

