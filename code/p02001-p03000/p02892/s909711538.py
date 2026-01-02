#!/usr/bin/env python3
import sys
INF = float("inf")
from collections import deque

import sys
import math
from collections import defaultdict, deque
INF = float("inf")


class Graph(object):
    """グラフを扱うオブジェクト
    """

    def __init__(self, N):
        self.N = N
        self.E = [[] for _ in range(N)]
        pass

    def add_edge(self, from_, to_):
        """必ず0インデックスで入力すること。
        """
        self.E[from_].append((to_, 1))
        pass


def solve(N: int, S: "List[str]"):

    g = Graph(N)
    for i, s in enumerate(S):
        for j, c in enumerate(s):
            if c == "1":
                g.add_edge(i, j)

    ddd = -1
    for node in range(N):
        depth = [-2]*N
        q = deque()
        q.append((node, 1))
        while len(q) > 0:
            node, d = q.popleft()
            if depth[node] != -2:
                continue
            depth[node] = d
            for i, w in g.E[node]:
                if depth[i] == -2:
                    q.append((i, d+1))
                elif d == depth[i]:
                    print(-1)
                    return
        ddd = max(ddd, d)
    print(ddd)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(N)]  # type: "List[str]"
    solve(N, S)


if __name__ == '__main__':
    main()
