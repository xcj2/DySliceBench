#### import ####
import sys
import math
from collections import defaultdict

#### 設定 ####
sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

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

#a!をmodしつつ求める
def fact(a,M=mod):
    ans = 1
    for i in range(2,a+1):
        ans = ans*i
        ans = ans%M
    return ans


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


#aの逆元(mod M)を求める（aとMは互いに素であることが前提）
def mod_inv(a,M=mod):
    x = extgcd(a,M)[0]
    return (M+x%M)%M

N,K = II()

inv = [0]*(N+1)
for i in range(N+1):
    inv[i] = mod_inv(fact(i))

kfact = fact(K-1)
nfact = fact(N-K+1)

for i in range(1,K+1):
    if N-K+1-i < 0:
        print(0)
    else:
        ans = kfact*inv[i-1]*inv[K-i]*nfact*inv[i]*inv[N-K+1-i]
        ans = ans%mod
        print(ans)