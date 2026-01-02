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
def main():
    N = I()
    G = [[] for _ in range(N)]
    edges = []
    edge2color = {}
    for _ in range(N-1):
        a, b = LI_()
        G[a].append(b)
        G[b].append(a)
        edges.append((a, b))
    K = -1
    for adj_v in G:
        K = max(K, len(adj_v))
    visited = [0] * N
    def colorGraph(v, parColor=-1):
        children = G[v]
        colorNum = 1
        visited[v] = 1
        for child_v in children:
            if visited[child_v]:
                continue
            if colorNum == parColor:
                colorNum += 1
            edge2color[(v, child_v)] = colorNum
            edge2color[(child_v, v)] = colorNum
            colorGraph(child_v, colorNum)
            colorNum += 1
    # import pdb
    # pdb.set_trace()
    colorGraph(0)
    print(K)
    for edge in edges:
        key = (edge[0], edge[1])
        print(edge2color[key])

main()

