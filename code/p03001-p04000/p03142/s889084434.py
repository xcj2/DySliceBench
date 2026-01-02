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
    N, M = read_values()

    L = [set() for _ in range(N)]
    C = [0] * N
    S = {i for i in range(N)}
    for _ in range(N + M - 1):
        u, v = read_index()
        L[u].add(v)
        C[v] += 1
        if v in S:
            S.remove(v)

    Q = queue.Queue()
    for s in S:
        Q.put(s)

    P = ["0"] * N    
    while not Q.empty():
        s = Q.get()
        for w in L[s]:
            P[w] = str(s + 1)
            C[w] -= 1
            if C[w] == 0:
                Q.put(w)

    print("\n".join(P))


if __name__ == "__main__":
    main()
