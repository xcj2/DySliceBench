import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
int1 = lambda x: int(x) - 1

class UnionFind:
    def __init__(self, n):
        self.state = [-1] * n
        self.weight = [0] * n
        self.state0 = []
        self.weight0 = []

    def save(self):
        self.state0 = self.state[:]
        self.weight0 = self.weight[:]

    def restore(self):
        self.state = self.state0[:]
        self.weight = self.weight0[:]

    def root(self, u):
        v = self.state[u]
        if v < 0: return u
        self.state[u] = res = self.root(v)
        return res

    def merge(self, u, v):
        ru = self.root(u)
        rv = self.root(v)
        if ru == rv: return
        du = self.state[ru]
        dv = self.state[rv]
        if du > dv: ru, rv = rv, ru
        if du == dv: self.state[ru] -= 1
        self.state[rv] = ru
        self.weight[ru] += self.weight[rv]
        return

    def get_weight(self, u):
        r = self.root(u)
        return self.weight[r]

def main():
    def dfs(u, w, ou=-1):
        for y, ku, i in to[u]:
            if ku == ou: continue
            if y > w: continue
            if use_edge[i]:continue
            use_edge[i] = True
            dfs(ku, w, u)

    to = defaultdict(list)
    n, m = map(int, input().split())
    xx = list(map(int, input().split()))
    uf = UnionFind(n)
    for i, x in enumerate(xx):
        uf.weight[i] = x
    edges = []
    for i in range(m):
        a, b, y = map(int, input().split())
        a, b = a - 1, b - 1
        edges.append([y, a, b, i])
        to[a].append([y, b, i])
        to[b].append([y, a, i])
    edges.sort()
    max_edge_candidate = []
    use_edge = [False] * m
    for y, a, b, i in edges:
        uf.merge(a, b)
        if y <= uf.get_weight(a):
            max_edge_candidate.append([y, a, b, i])
    while max_edge_candidate:
        y, a, b, i = max_edge_candidate.pop()
        if use_edge[i]: continue
        dfs(a, y)
    print(m-sum(use_edge))

main()
