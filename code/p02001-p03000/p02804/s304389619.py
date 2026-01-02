# coding: utf-8
# Your code here!
import sys
sys.setrecursionlimit(10000000)

N,K=map(int,input().split())

A=list(map(int,input().split()))
A.sort()

mod=10**9+7
cand=[0]

#互いに素なa,bについて、a*x+b*y=1の一つの解
def extgcd(a,b):
    r = [1,0,a]
    w = [0,1,b]
    while w[2]!=1:
        q = r[2]//w[2]
        r2 = w
        w2 = [r[0]-q*w[0],r[1]-q*w[1],r[2]-q*w[2]]
        r = r2
        w = w2
    #[x,y]
    return [w[0],w[1]]

# aの逆元(mod m)を求める。(aとmは互いに素であることが前提)
def mod_inv(a,m):
    x = extgcd(a,m)[0]
    return (m+x%m)%m

def comb(n):
    if n==N-1:
        return 0
    
    if n<K-2:
        cand.append(0)
    elif n==K-2:
        cand.append(1)
    else:
        cand.append((cand[-1]*n)%mod*mod_inv((n-K+2),mod)%mod)
        
    comb(n+1)
    
    return 0

comb(0)

for i in range(N-1):
    cand[i+1]=cand[i]+cand[i+1]

up=sorted(A)
down=sorted(A,reverse=True)
down=list(map(lambda x:-x,down))

ans=0
for i in range(N):
    ans+=(up[i]+down[i])*cand[i]

print(int(ans%mod))