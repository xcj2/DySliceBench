import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools
from collections import deque

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

DR = [1, -1, 0, 0]
DC = [0, 0, 1, -1]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()


def reach_all(G, N):
    visited = [0] * N
    def dfs(G, v):
        visited[v] = 1
        for next_v in G[v]:
            if visited[next_v]:
                continue
            dfs(G, next_v)
    dfs(G, 0)
    if sum(visited) != N:
        return False
    return True

def main():
    N, M = LI()
    edge = []
    for _ in range(M):
        a, b = LI_()
        edge.append((a, b))

    cnt = 0
    for i in range(M):
        G = [[] for _ in range(N)]
        for j in range(M):
            if i == j:
                continue
            a, b = edge[j]
            G[a].append(b)
            G[b].append(a)
        if not reach_all(G, N):
            cnt += 1
    print(cnt)
main()

