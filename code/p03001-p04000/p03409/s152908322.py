#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)


class BipartiteMatch(object):

    def __init__(self, n):
        self.n = n
        self.conns = [[] for _ in range(n)]
        self.matched = [-1] * n
        self.visited = None
    def add_edge(self, s, t):
        self.conns[s].append(t)
        self.conns[t].append(s)

    def _dfs(self, i):
        self.visited[i] = True
        for j in self.conns[i]:
            k = self.matched[j]
            if (k < 0 or (not self.visited[k] and self._dfs(k))):
                self.matched[i] = j
                self.matched[j] = i
                return True
        return False

    def run(self):
        ret = 0
        for i in range(self.n):
            if self.matched[i] >= 0:
                continue
            self.visited = [False] * self.n
            if self._dfs(i):
                ret += 1
        return ret

def solve(N: int, a: "List[int]", b: "List[int]", c: "List[int]", d: "List[int]"):
    bm = BipartiteMatch(N * 2)
    for i, (x, y) in enumerate(zip(a, b)):
        for j, (xx, yy) in enumerate(zip(c, d)):
            if x < xx and y < yy:
                #print(i, N + j)
                bm.add_edge(i, N + j)
    ret = bm.run()
    print(ret)
    return

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
