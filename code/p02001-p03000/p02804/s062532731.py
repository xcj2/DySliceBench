def i1():
 return int(input())
def i2():
 return [int(i) for i in input().split()]

[N,K]=i2()
a=i2()
mod = 10**9+7
c=[0 for i in range(N+1)]
ci=[0 for i in range(N+1)]
c[0]=1
for i in range(1,N+1):
 c[i]=c[i-1]*i
 c[i]%=mod
def bp(x,n):
        r=1
        while(n):
           if n%2:
              r=r*x%mod
           x=x*x%mod
           n>>=1
        return r
for i in range(N+1):
  ci[i]=bp(c[i],10**9+5)
ans=0
a.sort()
for i in range(N):
 if i>=K-1:
   ans+=a[i]*((c[i]*ci[i-K+1]*ci[K-1])%mod)
 if i<=N-K:
   ans-=a[i]*((c[N-i-1]*ci[N-i-1-K+1]*ci[K-1])%mod)
 ans%=mod
print(ans%mod)