# coding: utf-8
# Your code here!

def MI():return map(int,input().split())
def LI():return list(MI())

N,K=map(int,open(0).read().split())

# from juppyさん
mod = 10**9+7
MAX_N = 20020

fact = [1]
fact_inv = [0]*(MAX_N+4)
for i in range(MAX_N+3):
    fact.append(fact[-1]*(i+1)%mod)

fact_inv[-1] = pow(fact[-1],mod-2,mod)
for i in range(MAX_N+2,-1,-1):
    fact_inv[i] = fact_inv[i+1]*(i+1)%mod


def mod_comb_k(n,k,mod):
    return fact[n] * fact_inv[k] % mod * fact_inv[n-k] %mod
    
# ここまで

for i in range(1,K+1):
    if N-K+1<i:print(0);continue
    ans=mod_comb_k(N-K+1,i,mod)*mod_comb_k(K-1,i-1,mod)
    print(ans%mod)