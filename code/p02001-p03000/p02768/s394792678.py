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

# 互いに素なa,bについて、a*x+b*y=1の一つの解[x,y]を出力
def extgcd(a,b):
    r = [1,0,a]
    w = [0,1,b]
    while w[2] != 1:
        q = r[2]//w[2]
        r2 = w
        w2 = [r[0]-q*w[0],r[1]-q*w[1],r[2]-q*w[2]]
        r = r2
        w = w2
    return [w[0],w[1]]

# aの逆元(mod M)を求める（aとMは互いに素）
def mod_inv(a,M=mod):
    x = extgcd(a,M)[0]
    return (M+x%M)%M

def nCk2(n,k):
    x = [0]*(k+1)
    x[0] = 1
    for i in range(1,k+1):
        x[i] = x[i-1]*(n-k+i)*mod_inv(i) % mod
    return x[-1]

n,a,b = LI()

ans = pow(2,n,mod)-1
ans -= nCk2(n,a)
ans %= mod
ans -= nCk2(n,b)
ans %= mod

print(ans)