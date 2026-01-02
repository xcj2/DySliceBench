#### import ####
import sys
import math
from collections import defaultdict

#### 設定 ####
sys.setrecursionlimit(10**7)

#### 定数 ####
mod = 10**9 + 7

#### 読み込み ####
def I(): return int(input())
def II(): return map(int, input().split())
def III(): return list(map(int, input().split()))
def Line(N):
    read_all = [tuple(map(int, input().split())) for _ in range(N)]
    return map(list,zip(*read_all))

#################

#互いに素なa,bについて、a*x+b*y=1の一つの解[x,y]を出力
def extgcd(a,b):
    r = [1,0,a]
    w = [0,1,b]
    while w[2]!=1:
        q = r[2]//w[2]
        r2 = w
        w2 = [r[0]-q*w[0],r[1]-q*w[1],r[2]-q*w[2]]
        r = r2
        w = w2
    return [w[0],w[1]]

# aの逆元(mod M)を求める（aとMは互いに素であることが前提）
def mod_inv(a,M=mod):
    x = extgcd(a,M)[0]
    return (M+x%M)%M

#a!をmodしつつ求める
def fact(a,M=mod):
    ans = 1
    for i in range(2,a+1):
        ans = ans*i
        ans = ans%M
    return ans


p = I()
a = III()

beki = [[1]*p for _ in range(p)]
for i in range(p):
    for j in range(1,p):
        beki[i][j] = beki[i][j-1]*(-i)
        beki[i][j] = beki[i][j]%p

fact_inv = [0]*p
for i in range(p):
    fact_inv[i] = mod_inv(fact(i,p),p)

pfact = fact(p-1,p)

ans = [0]*p
for j in range(p):
    if a[j]==0:
        continue
    else:
        ans[0] += 1
        for i in range(p):
            ans[i] -= pfact*fact_inv[i]*fact_inv[p-1-i]*beki[j][p-1-i]
            ans[i] %= p

print(*ans)