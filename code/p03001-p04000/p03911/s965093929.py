import bisect
import copy
import heapq
import sys
import itertools
import queue
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
mod = 10 ** 9 + 7

def read_values(): return map(int, input().split())
def read_index(): return map(lambda x: int(x) - 1, input().split())
def read_list(): return list(read_values())
def read_lists(N): return [read_list() for n in range(N)]
def init_dp1(init, N): return [init for _ in range(N)]
def init_dp2(init, N, M): return [[init for _ in range(M)] for _ in range(N)]


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


def main():
    N, M = read_values()
    uf = UF(N + M)
    for i in range(N):
        L = read_list()
        for l in L[1:]:
            uf.make_pair(i, l - 1 + N)

    for n in range(1, N):
        if not uf.is_pair(0, n):         
            print("NO")
            return
    print("YES")


if __name__ == "__main__":
    main()
