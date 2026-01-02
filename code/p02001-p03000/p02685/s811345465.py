import bisect
import copy
import heapq
import math
import sys
from collections import *
from itertools import accumulate, combinations, permutations, product
from math import gcd
def input():
    return sys.stdin.readline()[:-1]
def ruiseki(lst):
    return [0]+list(accumulate(lst))
mod=998244353
al=[chr(ord('a') + i) for i in range(26)]
direction=[[1,0],[0,1],[-1,0],[0,-1]]

n,m,k=map(int,input().split())

# MOD combination
def cmb(n, r, mod=998244353):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

N = 10**5*2+100
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, N + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )

ans=m*pow(m-1,n-1,mod)
ans%=mod
# print(ans)
for i in range(k):
    tmp=cmb(n-1,i+1)*m*pow(m-1,n-(i+2),mod)
    # print(cmb(n-1,i+1),m,pow(m-1,n-(i+1),mod))
    # print(tmp)
    tmp%=mod
    ans+=tmp
    ans%=mod
    # print(ans,tmp)
print(ans)