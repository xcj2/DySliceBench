class segment_tree:
    def __init__(self, N, operator_M, e_M):
        self.op_M = operator_M
        self.e_M = e_M
        
        self.N0 = 1<<(N-1).bit_length()
        self.dat = [self.e_M]*(2*self.N0)
    
    # 長さNの配列 initial で初期化
    def build(self, initial):
        self.dat[self.N0:self.N0+len(initial)] = initial[:]
        for k in range(self.N0-1,0,-1):
            self.dat[k] = self.op_M(self.dat[2*k], self.dat[2*k+1])

    # a_k の値を x に更新
    def update(self,k,x):
        k += self.N0
        self.dat[k] = x
        k //= 2
        while k:
            self.dat[k] = self.op_M(self.dat[2*k], self.dat[2*k+1])
            k //= 2

    # 区間[L,R]をopでまとめる
    def query(self,L,R):
        L += self.N0; R += self.N0 + 1 
        sl = sr = self.e_M
        while L < R:
            if R & 1:
                R -= 1
                sr = self.op_M(self.dat[R],sr)
            if L & 1:
                sl = self.op_M(sl,self.dat[L])
                L += 1
            L >>= 1; R >>= 1
        return self.op_M(sl,sr)

    def get(self, k): #k番目の値を取得。query[k,k]と同じ
        return self.dat[k+self.N0]


# coding: utf-8
# Your code here!

import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline
read = sys.stdin.read

n = int(input())
xd = [[int(i) for i in readline().split()] for _ in range(n)]
xd.sort(key=lambda x: x[0])

xx = [xdi[0] for xdi in xd]
from bisect import bisect_left

a = [bisect_left(xx,x+d)-1 for x,d in xd]
seg = segment_tree(n, max, 0)
seg.build(a)

b = list(range(n))
for i in range(n-2,-1,-1):
    if i+1 <= a[i]:
        b[i] = seg.query(i+1,a[i])   
        seg.update(i,b[i])

dp = [0]*(n+1)
dp[-1] = 1

MOD = 998244353
for i in range(n-1,-1,-1):
    dp[i] = (dp[i+1] + dp[b[i]+1])%MOD

#print(a)
#print(b)
#print(dp)
print(dp[0])





