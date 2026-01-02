#!python3.8
# -*- coding: utf-8 -*-
# abc177/abc177_d
import sys
from collections import deque

s2nn = lambda s: [int(c) for c in s.split(' ')]
ss2nn = lambda ss: [int(s) for s in list(ss)]
ss2nnn = lambda ss: [s2nn(s) for s in list(ss)]
i2s = lambda: sys.stdin.readline().rstrip()
i2n = lambda: int(i2s())
i2nn = lambda: s2nn(i2s())
ii2ss = lambda n: [i2s() for _ in range(n)]
ii2nn = lambda n: ss2nn(ii2ss(n))
ii2nnn = lambda n: ss2nnn(ii2ss(n))

class node:
    def __init__(self, i):
        self.i = i
        self.adj = {self}
        self.visited = False
    
    def join(self, B):
        self.adj.add(B)
        B.adj.add(self)

def bfs(tar):
    q = deque()
    q.append(tar)
    cnt = 0
    while (q):
        tar = q.popleft()
        if not tar.visited:
            cnt += 1
        tar.visited = True
        q.extend(adj for adj in tar.adj if not adj.visited)
    return cnt

def main():
    N, M = i2nn()
    G = [node(i) for i in range(N + 1)]
    for _ in range(M):
        A, B = i2nn()
        G[A].join(G[B])
    ans = 0
    for tar in G[1:]:
        if not tar.visited:
            ans = max(bfs(tar), ans)
    print(ans)
    return

main()
