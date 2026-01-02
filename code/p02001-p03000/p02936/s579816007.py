
import bisect
import collections
import itertools


def getint(): return int(input())
def getints(): return list(map(int, input().split()))
def getint2d(rows): return [getints() for _ in range(rows)]
def getgrid(rows): return [input() for _ in range(rows)]
def array1d(n, value): return [value for _ in range(n)]
def array2d(n, m, value): return [array1d(m, value) for _ in range(n)]

class Graph:
    def __init__(self, node_count, edge_count):
        self.node_count = node_count
        self.lst = [-1 for _ in range(node_count)]
        self.nxt = [0 for _ in range(edge_count)]
        self.to = [0 for _ in range(edge_count)]
        self.m = 0

    def add_edge(self, u, v, w):  # bidirection weight
        m = self.m
        self.nxt[m], self.lst[u], self.to[m] = self.lst[u], m, (v, w)
        self.m += 1

    def traverse(self, u):
        m = self.lst[u]
        while m != -1:
            yield self.to[m]
            m = self.nxt[m]


n,q=getints()
values = [0]*n
gr = Graph(n,2*n)

for _ in range(n-1):
    a,b=getints()
    a,b=a-1,b-1
    gr.add_edge(a,b,1)
    gr.add_edge(b,a,1)

for _ in range(q):
    u, p=getints()
    values[u-1] += p

def distribute(u, par, prev):
    stk = []
    stk.append((u, par, 0))
    while stk:
        u,par,prev=stk[-1]
        stk.pop()
        values[u] += prev
        for v, _ in gr.traverse(u):
            if v == par: continue
            stk.append((v,u,values[u]))

distribute(0, -1, 0)
print(" ".join(map(str, values)))