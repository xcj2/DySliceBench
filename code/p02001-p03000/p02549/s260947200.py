# -*- coding: utf-8 -*-
import sys 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
MOD = 998244353

class BIT2:
    def __init__(self, N):
        self.N = (N+1)
        self.data0 = [0] * (N+1)
        self.data1 = [0] * (N+1)
        
    def _add(self, data, k, x):
        while k < self.N: #k <= Nと同義
            data[k] += x
            k += k & -k

    def _sum(self, data, k):
        s = 0
        while k:
            s += data[k]
            k -= k & -k
        return s

    def add(self, l, r, x):
        self._add(self.data0, l, -x*(l-1))
        self._add(self.data0, r, x*(r-1))
        self._add(self.data1, l, x)
        self._add(self.data1, r, -x)

    def sum(self, l, r):
        return self._sum(self.data1, r-1) * (r-1) + self._sum(self.data0, r-1) - self._sum(self.data1, l-1) * (l-1) - self._sum(self.data0, l-1)
    
N, K = map(int, readline().split())
bit = BIT2(N)
d = []
for _ in range(K):
    L,R = map(int, readline().split())
    d.append((L,R))

bit.add(1,2,1)

for i in range(2,N+1):
    for k in range(K):
        L,R = d[k]
        tmp = bit.sum(max(1,i-R),max(1,i-L+1))%MOD
        bit.add(i,i+1,tmp)
print(bit.sum(N,N+1)%MOD)