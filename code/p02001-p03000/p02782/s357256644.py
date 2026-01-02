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

# 0!~n!をmodしつつ求める
def fact_all(n,M=mod):
    f = [1]*(n+1)
    ans = 1
    for i in range(1,n+1):
        ans = (ans*i)%M
        f[i] = ans
    return f

# inv(0!)~inv(n!)をmodしつつ求める
def fact_inv_all(fact_all,M=mod):
    N = len(fact_all)
    finv = [0]*N
    finv[-1] = pow(fact_all[-1],M-2,M)
    for i in range(N-1)[::-1]:
        finv[i] = finv[i+1]*(i+1)%M
    return finv

# nCkをmodしつつ返す
def nCk(n,k,fact_list=[],inv_list=[],M=mod):
    # a!をmodしつつ求める
    def fact(a,M=mod):
        ans = 1
        for i in range(2,a+1):
            ans = (ans*i)%M
        return ans

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
    
    if fact_list and inv_list:
        return (((fact_list[n]*inv_list[k])%M)*inv_list[n-k])%M
    else:
        x = fact(n,M)
        y1 = mod_inv(fact(k,M),M)
        y2 = mod_inv(fact(n-k,M),M)
        return ((x*y1)%M*y2)%M


def g(r,c):
    retval = 0
    for i in range(r+1):
        retval += nCk(i+c+1,c,fact_list,inv_list)
        retval %= mod
    return retval

r1,c1,r2,c2 = LI()
fact_list = fact_all(r2+c2+1)
inv_list = fact_inv_all(fact_list)

print((g(r2,c2)-g(r2,c1-1)-g(r1-1,c2)+g(r1-1,c1-1))%mod)