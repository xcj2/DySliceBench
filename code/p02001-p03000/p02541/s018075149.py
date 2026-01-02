def prime_factorize(N): #素因数分解
    exponent = 0
    while N%2 == 0:
        exponent += 1
        N //= 2
    #if exponent: factorization = [[2,exponent]]
    if exponent: factorization = [[1,pow(2,exponent)]]
    else: factorization = []
    i=1
    while i*i <=N:
        i += 2
        if N%i: continue
        exponent = 0
        while N%i == 0:
            exponent += 1
            N //= i
        factorization.append([1,pow(i,exponent)])
        #factorization.append([i,exponent])
    #if N!= 1: factorization.append([N,1])
    if N!= 1: factorization.append([1,N])
    assert N != 0, "zero"
    return factorization

def Garner_NOmod(alst,mlst):
    x = 0; M = 1
    # 互いに素を仮定
    for a,m in zip(alst,mlst):
        c = (a-x)*modinv(M,m)%m
        x += c*M
        M *= m
    return x

def extgcd(x,y):
    if y==0: return 1,0 #g=x
    r0,r1,s0,s1 = x,y,1,0
    while r1 != 0:
        r0,r1, s0,s1 = r1,r0%r1, s1,s0-r0//r1*s1
    #g = r0
    return s0,(r0-s0*x)//y
    
def modinv(a,MOD):
    x,y = extgcd(a,MOD)
    return x%MOD

# coding: utf-8
# Your code here!
import sys
readline = sys.stdin.readline
read = sys.stdin.read

n, = map(int, readline().split())
#lr = [list(map(int, readline().split())) for _ in range(q)]

if n==1:
    print(1)
    exit()

lst = prime_factorize(2*n)

res = []
from itertools import product
for a in product(*lst):
    v = 1
    for i in a: v*= i
    w = 2*n//v
    res.append(Garner_NOmod([0,w-1],[v,w]))

res.sort()
"""
for i in res:
    #print(n,i,i*(i+1)//2)
    assert (i*(i+1)//2)%(n)==0
"""

print(res[1])

