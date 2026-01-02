def fact(n):
    global mod
    if n==0:
        return 1
    else:
        res=1
        for i in range(1,n+1):
            res=(res*i)%mod
        return res

def inv(n):
    global mod
    res=1
    prod=n%mod
    a=mod-2
    while a>0:
        if a%2==1:
            res=(res*prod)%mod
        a//=2
        prod=(prod**2)%mod
    return res

def combi(n,r):
    return (fact(n)*inv(fact(r))*inv(fact(n-r)))%mod

def ord(n,p):
    res=0
    while n%p==0:
        res+=1
        n//=p
    return res

mod=10**9+7
N,M=map(int,input().split())
l=[]

if ord(M,2)>0:
    l.append(ord(M,2))
    M//=2**ord(M,2)

p=3
while M>1 and p<=int(10**4.5):
    if ord(M,p)>0:
        l.append(ord(M,p))
        M//=p**ord(M,p)
    p+=2
if M>1:
    l.append(1)
    M=1

ans=1
for e in l:
    ans=(ans*combi(e+N-1,N-1))%mod

print(ans)