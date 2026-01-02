import sys
import math
from collections import defaultdict

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def II(): return map(int, input().split())
def III(): return list(map(int, input().split()))
def Line(N,num):
    if N<=0:
        for _ in range(num): return []
    elif num==1:
        return [I() for _ in range(N)]
    else:
        read_all = [tuple(map(int, input().split())) for _ in range(N)]
        return map(list,zip(*read_all))

#################

class SegmentTree:
    def __init__(self,N,default):
        #演算の定義
        self.op = min
        #初期化の値
        self.default = default
        self.N0 = 2**(N-1).bit_length()
        self.tree = [self.default]*(2*self.N0)
        
    #a_kの値をxに更新
    def update(self,k,x):
        k += self.N0-1
        self.tree[k] = x
        while k >= 0:
            k = (k-1)//2
            self.tree[k] = self.op(self.tree[2*k+1], self.tree[2*k+2])

    #区間[l,r]へのクエリ
    def query(self,l,r):
        L = l + self.N0; R = r + self.N0 + 1 
        s = self.default
        while L < R:
            if R & 1:
                R -= 1
                s = self.op(s,self.tree[R-1])
            if L & 1:
                s = self.op(s,self.tree[L-1])
                L += 1
            L >>= 1; R >>= 1
        return s

    #k番目の値を取得
    def get(self,k):
        return self.tree[k+self.N0-1]

class Max_SegmentTree:
    def __init__(self,N,default):
        #演算の定義
        self.op = max
        #初期化の値
        self.default = default
        self.N0 = 2**(N-1).bit_length()
        self.tree = [self.default]*(2*self.N0)
        
    #a_kの値をxに更新
    def update(self,k,x):
        k += self.N0-1
        self.tree[k] = x
        while k >= 0:
            k = (k-1)//2
            self.tree[k] = self.op(self.tree[2*k+1], self.tree[2*k+2])

    #区間[l,r]へのクエリ
    def query(self,l,r):
        L = l + self.N0; R = r + self.N0 + 1 
        s = self.default
        while L < R:
            if R & 1:
                R -= 1
                s = self.op(s,self.tree[R-1])
            if L & 1:
                s = self.op(s,self.tree[L-1])
                L += 1
            L >>= 1; R >>= 1
        return s

    #k番目の値を取得
    def get(self,k):
        return self.tree[k+self.N0-1]

from bisect import bisect_left

N,K = II()
P = III()

seg = SegmentTree(N,N+1)
for i in range(N):
    seg.update(i,P[i])

kmin = [False]*N
for i in range(N-K+1):
    a = seg.query(i,i+K-1)
    if a==P[i]:
        kmin[i] = True

seg2 = Max_SegmentTree(N,-1)
for i in range(N):
    seg2.update(i,P[i])

kmax = [False]*N
for i in range(K-1,N):
    a = seg2.query(i-K+1,i)
    if a==P[i]:
        kmax[i] = True

dp = [0]*N
dp[K-1] = 1
flag = True
bad_p = []
for i in range(K-1):
    if P[i]>P[i+1]:
        flag = False
for i in range(N-1):
    if P[i]>P[i+1]:
        bad_p.append(i)

for i in range(K,N):
    now_flag = False
    if kmax[i]:
        if kmin[i-K]:
            dp[i] = dp[i-1]
        else:
            l = bisect_left(bad_p,i-K+1)
            r = bisect_left(bad_p,i)
            if l==r:
                now_flag = True
            if flag and now_flag:
                dp[i] = dp[i-1]
            else:
                dp[i] = dp[i-1]+1
    else:
        dp[i] = dp[i-1]+1

    if now_flag:
        flag = True

print(dp[N-1])