#!/usr/bin/env python3
import sys
INF = float("inf")
from collections import deque


class Dinic:
    def __init__(self, n):
        self.n = n
        self.links = [[] for _ in range(n)]
        self.depth = None
        self.progress = None

    def add_edge(self, _from, to, cap):
        self.links[_from].append([cap, to, len(self.links[to])])
        self.links[to].append([0, _from, len(self.links[_from]) - 1])

    def bfs(self, s):
        depth = [-1] * self.n
        depth[s] = 0
        q = deque([s])
        while q:
            v = q.popleft()
            for cap, to, rev in self.links[v]:
                if cap > 0 and depth[to] < 0:
                    depth[to] = depth[v] + 1
                    q.append(to)
        self.depth = depth

    def dfs(self, v, t, flow):
        if v == t:
            return flow
        links_v = self.links[v]
        for i in range(self.progress[v], len(links_v)):
            self.progress[v] = i
            cap, to, rev = link = links_v[i]
            if cap == 0 or self.depth[v] >= self.depth[to]:
                continue
            d = self.dfs(to, t, min(flow, cap))
            if d == 0:
                continue
            link[0] -= d
            self.links[to][rev][0] += d
            return d
        return 0

    def max_flow(self, s, t):
        flow = 0
        while True:
            self.bfs(s)
            if self.depth[t] < 0:
                return flow
            self.progress = [0] * self.n
            current_flow = self.dfs(s, t, float('inf'))
            while current_flow > 0:
                flow += current_flow
                current_flow = self.dfs(s, t, float('inf'))


def solve(N: int, a: "List[int]", b: "List[int]", c: "List[int]", d: "List[int]"):
    red = [[a[i], b[i]] for i in range(N)]
    blue = [[c[i], d[i]] for i in range(N)]

    # 最大マッチング問題として解く。
    dn = Dinic(2*N+2)
    for i, (rx, ry) in enumerate(red):
        dn.add_edge(0, i+1, 1)
    for j, (bx, by) in enumerate(blue):
        dn.add_edge(N+j+1, 2*N+1, 1)

    for i, (rx, ry) in enumerate(red):
        for j, (bx, by) in enumerate(blue):
            if rx < bx and ry < by:
                dn.add_edge(i+1, N+j+1, 1)

    ans = dn.max_flow(0, 2*N+1)
    print(ans)

    # print(dn.links)


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int()] * (N)  # type: "List[int]"
    b = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    c = [int()] * (N)  # type: "List[int]"
    d = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        c[i] = int(next(tokens))
        d[i] = int(next(tokens))
    solve(N, a, b, c, d)


if __name__ == '__main__':
    main()
