# -*- coding: utf-8 -*-
"""
Created on Fri May  8 12:10:59 2020

@author: ybt07
"""

import sys
sys.setrecursionlimit(3*10**5)  # 繰り返し制限

# 組み合わせ
N = 2*10**5   # 問題サイズに合わせて変えておく
MOD = 10**9 + 7

# modint
# https://qiita.com/wotsushi/items/c936838df992b706084c

class ModInt:
    def __init__(self, x):
        self.x = x % MOD

    def __str__(self):
        return str(self.x)

    __repr__ = __str__

    def __add__(self, other):
        return (
            ModInt(self.x + other.x) if isinstance(other, ModInt) else
            ModInt(self.x + other)
        )

    def __sub__(self, other):
        return (
            ModInt(self.x - other.x) if isinstance(other, ModInt) else
            ModInt(self.x - other)
        )

    def __mul__(self, other):
        return (
            ModInt(self.x * other.x) if isinstance(other, ModInt) else
            ModInt(self.x * other)
        )

    # / : 商。　逆元はフェルマーの小定理を利用している
    '''
    def __truediv__(self, other):
        return (
            ModInt(
                self.x * pow(other.x, MOD - 2, MOD)
            ) if isinstance(other, ModInt) else
            ModInt(self.x * pow(other, MOD - 2, MOD))
        )
    '''

    def __truediv__(self, other):
        return (
            ModInt(
                self.x * inv[other.x]
            ) if isinstance(other, ModInt) else
            ModInt(self.x * inv[other])
        )


    # ** : 指数
    def __pow__(self, other):
        return (
            ModInt(pow(self.x, other.x, MOD)) if isinstance(other, ModInt) else
            ModInt(pow(self.x, other, MOD))
        )

    # x が Modint、y が通常の int の場合に、y.__add__(x) に対して、何を適用するか、定義している（→ x.__add__(y)を呼べ） 
    __radd__ = __add__

    def __rsub__(self, other):
        return (
            ModInt(other.x - self.x) if isinstance(other, ModInt) else
            ModInt(other - self.x)
        )

    __rmul__ = __mul__

    def __rtruediv__(self, other):
        return (
            ModInt(
                other.x * pow(self.x, MOD - 2, MOD)
            ) if isinstance(other, ModInt) else
            ModInt(other * pow(self.x, MOD - 2, MOD))
        )

    def __rpow__(self, other):
        return (
            ModInt(pow(other.x, self.x, MOD)) if isinstance(other, ModInt) else
            ModInt(pow(other, self.x, MOD))
        )

def cmb(n, r):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return ModInt(fac[n] * facinv[r] * facinv[n-r])

fac = [1, 1] # 元テーブル
facinv = [1, 1] #逆元テーブル
inv = [0, 1] #逆元テーブル計算用テーブル

for i in range(2, N):
    fac.append( ( fac[-1] * i ) % MOD )
    inv.append( ( -inv[MOD % i] * (MOD//i) ) % MOD )
    facinv.append( (facinv[-1] * inv[-1]) % MOD )

# 部分木のDP値を求めていく
# u : 求める頂点
# 親（親側に辿らないように） p

def dfs(u, p = -1):

    global DP, CN, E
    
    tmp_ans = 1
    tmp_cn = 0  # （自分を含む）部分木のノード数

    # u から出ている頂点 v
    for v in E[u]:
        if v != p:  # 親への辺以外について
            DP[v], CN[v] = dfs(v, u)
            tmp_cn += CN[v]
            tmp_ans *= DP[v] * cmb(tmp_cn, CN[v])
    DP[u] = tmp_ans
    CN[u] = tmp_cn + 1
            
    return tmp_ans, tmp_cn + 1

# 各頂点の真のDP値を求めていく

def bfs(u, p=-1):
    
    global DP, E
    
    tmp_ans = DP[u]
    tmp_cn = 1
    
    for v in E[u]:  # 各vに対して「真のDP値」を求めていく
        if v == p:
            continue
            
        # DP[u] と DP[v] から DP[v <- u] を求める
        tmp_cn = N - CN[v]  # v から見たときの u の部分木の要素数
        # print(v+1,tmp_cn)
        # tmp_ans = DP[u] / DP[v] / cmb(N - 1, CN[v])
                
        # DP[u <- v] を使って、DP[v] を更新する
        # DP[v] = DP[v] * tmp_ans * cmb(N-1, tmp_cn)

        # print(v+1,tmp_cn)
        # tmp_ans = DP[u] / cmb(N - 1, CN[v])
                
        # DP[u <- v] を使って、DP[v] を更新する
        DP[v] = DP[u] * CN[v] / (N - CN[v]) 

        bfs(v, u)
    
    return

# 入力処理
N = int(input())  # 頂点数
E = [[] for _ in range(N)]  # 辺の情報

for _ in range(N - 1):
    a, b = map(int, input().split())
    E[a-1].append(b-1)  # 双方向の情報
    E[b-1].append(a-1)
    
DP = [ModInt(1)] * N
CN = [0] * N

dfs(0)
bfs(0)

for i in DP:
    print(i)