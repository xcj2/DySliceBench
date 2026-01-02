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
def Line(N):
    read_all = [tuple(map(int, input().split())) for _ in range(N)]
    return map(list,zip(*read_all))

#################

from collections import Counter

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


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


N,M = II()

fact = [1]*(N+100)
for i in range(1,N+100):
    fact[i] = fact[i-1]*i %mod

inv = [1]*(N+100)
for i in range(N+100):
    inv[i] = mod_inv(fact[i])

c = Counter(prime_factorize(M))
ans = 1
for k in c.keys():
    i = c[k]
    temp = fact[N-1+i]*inv[i]*inv[N-1]
    ans *= temp
    ans %= mod

print(ans)