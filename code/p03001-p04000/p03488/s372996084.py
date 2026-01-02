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
    S = input().strip()
    X, Y = read_values()
    F = list(map(len, S.split("T")))

    S = {F[0]}
    if len(F) >= 2:
        for x in F[2::2]:
            SS = set()
            for s in S:
                SS.add(s + x)
                SS.add(s - x)
            S = SS

    if not X in S:
        print("No")
        return
    
    S = {0}
    if len(F) >= 1:
        for x in F[1::2]:
            SS = set()
            for s in S:
                SS.add(s + x)
                SS.add(s - x)
            S = SS
    
    if not Y in S:
        print("No")
        return 
    
    print("Yes")


if __name__ == "__main__":
    main()
