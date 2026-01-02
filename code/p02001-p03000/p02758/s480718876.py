import sys
import math
from collections import defaultdict
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 998244353

def I(): return int(input())
def LI(): return list(map(int, input().split()))
def LIR(row,col):
    if row <= 0:
        return [[] for _ in range(col)]
    elif col == 1:
        return [I() for _ in range(row)]
    else:
        read_all = [LI() for _ in range(row)]
        return map(list, zip(*read_all))

#################

from operator import itemgetter

def index_sort(A):
    A_sort = sorted(enumerate(A),key=itemgetter(1))
    index = [a[0] for a in A_sort]
    sorted_A = [a[1] for a in A_sort]
    return index, sorted_A

# 一点更新セグメントツリー
## 更新：１点の値をxに更新する　　クエリ演算：op
## 0-indexed
class SegmentTree:
    def __init__(self,N,default):
        # 演算の定義
        self.op = max
        # 初期化の値
        self.default = default
        self.N0 = 2**(N-1).bit_length()
        self.tree = [self.default]*(2*self.N0)
        
    # k番目の値をxに更新
    def update(self,k,x):
        k += self.N0-1
        self.tree[k] = x
        while k >= 0:
            k = (k-1)//2
            self.tree[k] = self.op(self.tree[2*k+1], self.tree[2*k+2])

    # 区間[l,r]へのクエリ
    def query(self,l,r):
        L = l+self.N0
        R = r+self.N0+1 
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

    # k番目の値を取得
    def get(self,k):
        return self.tree[k+self.N0-1]

N = I()
X,D = LIR(N,2)

index,X = index_sort(X)
D = [D[i] for i in index]

# iを選んだときに除かれる右端
end = SegmentTree(N,0)
for i in range(N):
    end.update(i,i)
for i in range(N-1)[::-1]:
    p = bisect_right(X,X[i]+D[i]-1)
    val = end.query(i,p-1)
    end.update(i,val)

# i以降を自由に使って作れる場合の数
dp = [0]*N
dp[N-1] = 2
for i in range(N-1)[::-1]:
    dp[i] = dp[i+1]
    if end.get(i) == N-1:
        dp[i] += 1
    else:
        dp[i] += dp[end.get(i)+1]
    dp[i] %= mod

print(dp[0])