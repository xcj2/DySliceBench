# modulo:mod

# inverse x^(-1)
def inv(x):
    global mod
    return pow(x,mod-2,mod)

# factorial x!
def fact(x):
    global mod
    res=1
    for i in range(2,x+1):
        res=res*i%mod
    return res

# combination nCr
def combi(n,r):
    if r<0 or r>n:
        return 0
    else:
        return fact(n)*inv(fact(r))*inv(fact(n-r))%mod

mod=10**9+7

N=int(input())
x=[0]
x.extend(list(map(int,input().split())))
invs=[inv(d) for d in range(N)]
# print(invs)
ans=0;s=0
for d in range(1,(N-1)//2+1):
    s=(s+x[N-d]-x[d])%mod
    ans=(ans+s*invs[d]*invs[d+1])%mod
    if d!=N-d-1:
        ans=(ans+s*invs[N-d-1]*invs[N-d])%mod
for i in range(1,N):
    ans=(ans+(x[N]-x[i])*invs[N-i])%mod
ans=ans*fact(N-1)%mod

print(ans)