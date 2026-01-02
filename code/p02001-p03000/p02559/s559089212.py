class fenwick_tree:
    def __init__(self, n=0, T=int):
        self._n = n
        self.data = [T() for _ in range(n)]
        self.T = T
    
    def add(self, p, x):
        p += 1
        while p <= self._n:
            self.data[p - 1] += x
            p += p & -p
    
    def sum(self, l, r):
        return self._sum(r) - self._sum(l)
    
    def _sum(self, r):
        s = self.T()
        while r > 0:
            s += self.data[r - 1]
            r -= r & -r
        return s

import sys
input = sys.stdin.readline
n, q = map(int, input().split())
t = fenwick_tree(n)
a = list(map(int, input().split()))
for i in range(n):
    t.add(i, a[i])
for _ in range(q):
    qtype, op1, op2 = map(int, input().split())
    if qtype == 0:
        t.add(op1, op2)
    else:
        print(t.sum(op1, op2))