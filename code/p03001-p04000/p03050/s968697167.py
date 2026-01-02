import numpy as np
def eratosthenes(n):
    is_prime = np.ones((n+1,), dtype=bool)
    is_prime[:2] = False
    for i in range(2,n+1):
        if is_prime[i]:
            is_prime[i*2::i]=False
    return np.arange(n+1)[is_prime]
Ps = eratosthenes(1000007)
def divisor(n):
    for p in Ps:
        if p*p>n:return -1
        if n%p==0:return p
def prime_division(n):
    d={}
    while n>1:
        p=divisor(n)
        if p==-1:d[n]=d.get(n,0)+1;break
        else:d[p]=d.get(p,0)+1;n//=p
    return d

def z(n,k,v):
    if len(k)==1:
        return [n*k[0]**i for i in range(v[0]+1)]
    else:
        r=[]
        for i in range(v[0]+1):
             r+=z(n*k[0]**i,k[1:],v[1:])
        return r
def y(n):
    pd=prime_division(n)
    KV=[[k,v] for k,v in pd.items()]
    K=[k for k,v in KV]; V=[v for k,v in KV]
    return z(1,K,V)

N=int(input())
if N==1:print(0);exit()
r=0
#print(y(N))
for yk in y(N):
    if yk>1 and N//(yk-1) == N%(yk-1):
        r+=yk-1
print(r)