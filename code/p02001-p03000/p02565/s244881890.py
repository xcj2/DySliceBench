class StronglyConnectedComponents():
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.rev = [[] for _ in range(n)]

    def add_edge(self, fr, to):
        self.graph[fr].append(to)
        self.rev[to].append(fr)

    def scc_id(self):
        group = [0] * self.n
        order = []
        for s in range(self.n):
            if group[s]: continue
            stack = [s]
            group[s] = -1
            while stack:
                node = stack.pop()
                for adj in self.graph[node]:
                    if group[adj]: continue
                    group[adj] = -1
                    stack.append(node)
                    stack.append(adj)
                    break
                else:
                    order.append(node)
        cnt = 0
        for s in order[::-1]:
            if group[s] != -1: continue
            stack = [s]
            group[s] = cnt
            while stack:
                node = stack.pop()
                for adj in self.rev[node]:
                    if group[adj] != -1: continue
                    group[adj] = cnt
                    stack.append(adj)
            cnt += 1
        return group, cnt

    def scc(self):
        group, cnt = self.scc_id()
        res = [[] for _ in range(cnt)]
        for i in range(self.n):
            res[group[i]].append(i)
        return res

class TwoSAT():
    def __init__(self, n):
        self.n = n
        self.res = [0] * self.n
        self.scc = StronglyConnectedComponents(2 * n)

    def add_clause(self, i, f, j, g):
        #assert 0 <= i < self.n
        #assert 0 <= j < self.n
        self.scc.add_edge(2 * i + (not f), 2 * j + g)
        self.scc.add_edge(2 * j + (not g), 2 * i + f)

    def satisfiable(self):
        group, cnt = self.scc.scc_id()
        for i in range(self.n):
            if group[2 * i] == group[2 * i + 1]: return False
            self.res[i] = (group[2 * i] < group[2 * i + 1])
        return True

    def result(self):
        return self.res

import sys
input = sys.stdin.buffer.readline

N, D = map(int, input().split())
F = [tuple(map(int, input().split())) for _ in range(N)]

ts = TwoSAT(N)

for i in range(N - 1):
    x0, y0 = F[i]
    for j in range(i + 1, N):
        x1, y1 = F[j]
        if abs(x0 - x1) < D:
            ts.add_clause(i, 1, j, 1)
        if abs(x0 - y1) < D:
            ts.add_clause(i, 1, j, 0)
        if abs(y0 - x1) < D:
            ts.add_clause(i, 0, j, 1)
        if abs(y0 - y1) < D:
            ts.add_clause(i, 0, j, 0)

if ts.satisfiable():
    print('Yes')
    print('\n'.join(map(str, (f[r] for r, f in zip(ts.result(), F)))))
else:
    print('No')