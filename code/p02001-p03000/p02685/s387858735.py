N,M,K=map(int,input().split())
MOD=998244353

def inv(a):
  return pow(a,MOD-2,MOD)
fact=[0,1]
for i in range(2,N+1):
  fact.append((fact[-1]*i)%MOD)
def choose(n,r):
  if r==0 or r==n:
    return 1
  else:
    return fact[n]*inv(fact[r])*inv(fact[n-r])%MOD
exp=[1]

def pow_k(x,n):
    if n==0:
        return 1
    K=1
    while n>1:
        if n%2!=0:
            K=K*x%MOD
            x=x**2%MOD
            n=(n-1)//2
        else:
            x=x**2%MOD
            n=n//2
    return K*x%MOD 

ans=0
for i in range(K+1):
  ans+=(M*choose(N-1,i)*pow_k(M-1,N-1-i)%MOD)  
  ans%=MOD
print(ans)  

