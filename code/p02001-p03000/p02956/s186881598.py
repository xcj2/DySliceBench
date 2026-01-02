import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

import numpy as np

MOD = 998244353

N = int(readline())
m = map(int,read().split())
Y = [y for x,y in sorted(zip(m,m))] # Y座標昇順

# 座圧
Y_rank = {y:i for i,y in enumerate(sorted(Y),1)}
Y = [Y_rank[y] for y in Y]

class BIT():
    def __init__(self, max_n):
        self.size = max_n + 1
        self.tree = [0] * self.size
        
    def get_sum(self,i):
        s = 0
        while i:
            s += self.tree[i]
            i -= i & -i
        return s
 
    def add(self, i, x):
        while i < self.size:
            self.tree[i] += x
            i += i & -i

LD = [0] * N
bit = BIT(N)
for i,y in enumerate(Y):
    LD[i] = bit.get_sum(y)
    bit.add(y,1)

def cumprod(arr,MOD):
    L = len(arr); Lsq = int(L**.5+1)
    arr = np.resize(arr,Lsq**2).reshape(Lsq,Lsq)
    for n in range(1,Lsq):
        arr[:,n] *= arr[:,n-1]; arr[:,n] %= MOD
    for n in range(1,Lsq):
        arr[n] *= arr[n-1,-1]; arr[n] %= MOD
    return arr.ravel()[:L]

x = np.full(N+10,2,np.int64); x[0] = 1
pow2 = cumprod(x,MOD)

LD = np.array(LD,dtype=np.int32)
D = np.array(Y)-1
L = np.arange(N)
R = N-1-L
U = N-1-D
LU = L-LD
RU = U-LU
RD = D-LD

x = pow2[N] - 1 + pow2[LD] + pow2[RD] + pow2[RU] + pow2[LU]
x -= pow2[U] + pow2[D] + pow2[R] + pow2[L]

answer = x.sum() % MOD
print(answer)