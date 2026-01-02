import sys
input = sys.stdin.readline
from collections import *
from bisect import *

class BIT:
    def __init__(self, n):
        self.n = n
        self.bit = [0]*(n+1)

    def add(self, i, x):
        i += 1
        
        while i<=self.n:
            self.bit[i] += x
            i += i&(-i)

    def acc(self, i):
        s = 0
        
        while i>0:
            s += self.bit[i]
            i -= i&(-i)
        
        return s

N, D, A = map(int, input().split())
XH = [tuple(map(int, input().split())) for _ in range(N)]
XH.sort(key=lambda t: t[0])
Xs = [X for X, _ in XH]
bit = BIT(N+1)
ans = 0

for i in range(N):
    X = XH[i][0]
    H = max(0, XH[i][1]-A*bit.acc(i+1))
    cnt = (H+A-1)//A
    ans += cnt
    j = bisect_right(Xs, X+2*D)
    bit.add(i, cnt)
    bit.add(j, -cnt)

print(ans)