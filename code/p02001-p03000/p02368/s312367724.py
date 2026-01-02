
import sys
import math
import bisect
import heapq
import copy
sys.setrecursionlimit(1000000)
from collections import deque
from itertools import permutations

class SCC:

    def __init__(self,n):
        self.n = n
        self.Edge = [[] for _ in range(n)]
        self.REdge = [[] for _ in range(n)]
        self.vs = []
        self.used = [False]*n
        self.order = [0]*n

    def add_edge(self,from_,to):
        self.Edge[from_].append(to)
        self.REdge[to].append(from_)

    def dfs(self,v):
        self.used[v] = True
        for u in self.Edge[v]:
            if not self.used[u]:
                self.dfs(u)
        self.vs.append(v)

    def rdfs(self,v,k):
        self.used[v] = True
        self.order[v] = k
        for u in self.REdge[v]:
            if not self.used[u]:
                self.rdfs(u,k)

    def compute(self):
        self.used = [False]*self.n
        self.vs.clear()
        for i in range(self.n):
            if not self.used[i]:
                self.dfs(i)
        self.used = [False]*self.n
        k = 0
        for i in reversed(self.vs):
            if not self.used[i]:
                self.rdfs(i,k)
            k+=1
        return k


def main():
    v,e = map(int,input().split())
    scc = SCC(v) 
    for _ in range(e):
        a,b = map(int,input().split())
        scc.add_edge(a,b)
    k = scc.compute()
    n = int(input())
    for _ in range(n):
        a,b = map(int,input().split())
        print (int(scc.order[a]==scc.order[b]))


if __name__ == '__main__':
    main()


