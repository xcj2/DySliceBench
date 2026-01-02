import sys
import math
from collections import defaultdict

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

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

class UF():
    def __init__(self,n):
        self.par = [i for i in range(n)]
        self.rank = [0]*n
        self.size = [1]*n

    # x が属する集合の代表値を返す
    def find(self,x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = y = self.find(self.par[x])
            return y

    # x と y の集合を結合する
    def union(self,x,y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return
        else:
            if self.rank[px] < self.rank[py]:
                px, py = py, px
            if self.rank[px] == self.rank[py]:
                self.rank[px] += 1
            self.par[py] = px
            self.size[px] += self.size[py]
            return

    # x と y が同じ集合に属するか判定する
    def is_same(self,x,y):
        return self.find(x) == self.find(y)

    # x が属する集合の要素数を返す
    def get_size(self,x):
        return self.size[self.find(x)]

N = I()
P = LI()

uf = UF(N)
for i in range(N):
    if P[i] != -1:
        uf.union(i,P[i]-1)

n = []
for i in range(N):
    if P[i] == -1:
        n.append(uf.get_size(i))

if not n:
    ans = 0
    for i in range(N):
        if i != uf.find(i):
            ans += 1
    print(ans)
    exit()

K = len(n)

# beki[i] = i!
beki = [1]*K
for i in range(1,K):
    beki[i] = beki[i-1]*i
    beki[i] %= mod

# fact[i] = (N-1)^i
fact = [1]*(K+1)
for i in range(1,K+1):
    fact[i] = fact[i-1]*(N-1)
    fact[i] %= mod

# -1を含むグループのみを取り出して考える
# dp[i][j]: 0~i番目のグループのうち，計jグループから1個ずつ取り出す場合の数
dp = [[0]*(K+1) for _ in range(K)]
for i in range(K):
    for j in range(K+1):
        if j == 0:
            dp[i][0] = 1
        elif i == 0:
            if j == 1:
                dp[0][1] = n[0]
        elif i+1 < j:
            continue
        else:
            dp[i][j] = dp[i-1][j] + n[i]*dp[i-1][j-1]
            dp[i][j] %= mod

# roop[i][j]: 0~i番目のグループのうち，jグループを使ったループの場合の数
roop = [[0]*(K+1) for _ in range(K)]
for i in range(K):
    for j in range(K+1):
        if j == 0:
            roop[i][0] = 1
        elif i == 0:
            if j == 1:
                roop[0][1] = n[0]-1
        elif i+1 < j:
            continue
        else:
            if j == 1:
                roop[i][j] = roop[i-1][j] + beki[j-1]*(n[i]-1)*dp[i-1][j-1]
            else:
                roop[i][j] = roop[i-1][j] + beki[j-1]*n[i]*dp[i-1][j-1]
            roop[i][j] %= mod

# cases[j]: Kグループのうち，jグループを使ったループの場合の数
# ループに使わない要素の行き先（N-1通り）も考慮する
cases = [0]*(K+1)
for j in range(K+1):
    cases[j] = roop[K-1][j]*fact[K-j]
    cases[j] %= mod

num = pow(N-1,K,mod)
default = 0
for i in range(N):
    if i == uf.find(i):
        default += uf.get_size(i)-1
ans = num*(default+K)
ans %= mod

for j in range(1,K+1):
    ans -= cases[j]
    ans %= mod

print(ans)