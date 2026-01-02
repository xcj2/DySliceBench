import sys
input = sys.stdin.readline
from collections import *

def compress(l):
    l = list(set(l))
    l.sort()
    idx = defaultdict(int)

    for i in range(len(l)):
        idx[l[i]] = i
    
    return idx
    
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

N = int(input())
xy = [tuple(map(int, input().split())) for _ in range(N)]
xy.sort(key=lambda t: t[0])
idx = compress([xy_i[1] for xy_i in xy])
lbit = BIT(N)
rbit = BIT(N)

for i in range(N):
    rbit.add(i, 1)
    
ans = 0
MOD = 998244353

for i in range(N):
    y = xy[i][1]
    rbit.add(idx[y], -1)
    a = i-lbit.acc(idx[y])
    b = lbit.acc(idx[y])
    c = rbit.acc(idx[y])
    d = N-1-i-rbit.acc(idx[y])
    add = 2*pow(2, N-1, MOD)-1
    pa = pow(2, a, MOD)
    pb = pow(2, b, MOD)
    pc = pow(2, c, MOD)
    pd = pow(2, d, MOD)
    add = (add-(pa-1))%MOD
    add = (add-(pb-1))%MOD
    add = (add-(pc-1))%MOD
    add = (add-(pd-1))%MOD
    add = (add-(pa*pb-pa-pb+1))%MOD
    add = (add-(pb*pc-pb-pc+1))%MOD
    add = (add-(pc*pd-pc-pd+1))%MOD
    add = (add-(pd*pa-pd-pa+1))%MOD
    ans += add
    ans %= MOD
    lbit.add(idx[y], 1)

print(ans)