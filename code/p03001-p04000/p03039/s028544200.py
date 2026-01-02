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
        return [[]]*num
    elif num==1:
        return [I() for _ in range(N)]
    else:
        read_all = [tuple(II()) for _ in range(N)]
        return map(list, zip(*read_all))

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


#aの逆元(mod M)を求める（aとMは互いに素）
def mod_inv(a,M=mod):
    x = extgcd(a,M)[0]
    return (M+x%M)%M

N,M,K = II()
ans = 0
for i in range(N):
    x = i*(i+1)//2 + (N-1-i)*(N-i)//2
    for j in range(M):
        ans += M*x + N*(j*(j+1)+(M-1-j)*(M-j))//2
        ans %= mod

ans = ans*fact(N*M-2)*mod_inv(fact(K-2))*mod_inv(fact(N*M-K))*mod_inv(2)
ans %= mod
print(ans)