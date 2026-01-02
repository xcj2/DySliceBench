import bisect
import copy
import heapq
import sys
import itertools
import math
import queue
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
# mod = 10 ** 9 + 7

def read_values(): return map(int, input().split())
def read_index(): return map(lambda x: int(x) - 1, input().split())
def read_list(): return list(read_values())
def read_lists(N): return [read_list() for n in range(N)]
def init_dp1(init, N): return [init for _ in range(N)]
def init_dp2(init, N, M): return [[init for _ in range(M)] for _ in range(N)]


def bfs(N, L):
    P = [0] * N
    Q = queue.Queue()
    Q.put(0)
    close = {0}
    while not Q.empty():
        v = Q.get()

        close.add(v)
        for w in L[v]:
            if w in close:
                continue
            close.add(w)
            P[w] = v
            Q.put(w)
    return P


def main():
    N, M = read_values()
    L = {i: set() for i in range(N)} 
    
    for _ in range(M):
        i, j = read_index()
        L[i].add(j)
        L[j].add(i)

    P = bfs(N, L)

    if -1 in P[1:]:
        print("No")
        return
    
    print("Yes")
    
    for p in P[1:]:
        print(p + 1)


if __name__ == "__main__":
    main()

