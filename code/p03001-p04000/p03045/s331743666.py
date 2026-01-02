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


class UF:
    def __init__(self, N):
        self.parent = [i for i in range(N)]
    
    def get_parent(self, a):
        p = self.parent[a]
        if a == p:
            return a
        
        q = self.get_parent(p)
        self.parent[a] = q
        return q

    def make_pair(self, a, b):
        pa = self.get_parent(a)
        pb = self.get_parent(b)
        if pa == pb:
            return
        
        self.parent[pa] = pb
        self.parent[a] = pb
    
    def is_pair(self, a, b):
        return self.get_parent(a) == self.get_parent(b)

    def num_group(self):
        return sum(1 for i, j in enumerate(self.parent) if i == j)


def main():
    N, M = read_values()
    uf = UF(N)
    
    for _ in range(M):
        X, Y, _ = read_index()
        uf.make_pair(X, Y)

    print(uf.num_group())


if __name__ == "__main__":
    main()
