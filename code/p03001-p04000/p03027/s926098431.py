p=1000003
def inv(x):
    return pow(x,p-2,p)
def exponen(a,b):
    return pow(a,b,p)
Fact=[0 for i in range(p)]
Fact[0]=1
for i in range(p-1):
    Fact[i+1]=((i+1)*Fact[i])%p
def fact(k):
    if 0<=k<p:
        return Fact[k]
    else:
        return 0
def solve(x,d,n):
    if x==0:
        return 0
    if d==0:
        return exponen(x,n)
    a=(x*inv(d))%p
    check=(-a)%p
    if 0<=check<=n-1:
        return 0
    return (exponen(d,n)*(fact(n-1+a)*inv(fact(a-1)))%p)%p

Q=int(input())
for i in range(Q):
    xi,di,ni=map(int,input().split())
    print(solve(xi,di,ni))

    
