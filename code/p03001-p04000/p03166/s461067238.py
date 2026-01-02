#!/usr/bin/env python3
import sys
from collections import defaultdict
from collections import deque

INF = float("inf")


class Graph(object):
    def __init__(self, N):
        self.N = N
        self.E = defaultdict(list)

    def add_edge(self, f, t, w=1):
        self.E[f].append((t, w))


def Topological_sorting(g):
    in_deg = [0]*g.N
    for i in range(g.N):        # ２重ループでO(E)
        for to_, _ in g.E[i]:
            in_deg[to_] += 1

    ans = [v for v in range(g.N) if in_deg[v] == 0]
    deq = deque(ans)

    while deq:                  # O(V+E)
        v = deq.popleft()
        for t, _ in g.E[v]:
            in_deg[t] -= 1
            if in_deg[t] == 0:
                ans.append(t)
                deq.append(t)
    if len(ans) != g.N:
        return False
    return ans


def solve(N: int, M: int, x: "List[int]", y: "List[int]"):
    g = Graph(N)
    for xx, yy in zip(x, y):
        g.add_edge(xx-1, yy-1)

    tsg = Topological_sorting(g)

    DP = [0]*N
    for i in tsg:
        for to, _ in g.E[i]:
            DP[to] = max(DP[i]+1, DP[to])
    print(max(DP))

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    x = [int()] * (M)  # type: "List[int]"
    y = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
    solve(N, M, x, y)


if __name__ == '__main__':
    main()
