import math

def modpow(a,b,mod=10**9+7):
    res=1
    a%=mod
    leng=int(math.log2(b))
    for i in range(leng,-1,-1):
        res=(res*res)%mod
        if (b>>i)&1:
            res=(res*a)%mod
    return res

def fact(x):
    ans=1
    for i in range(2,x+1):
        ans = (ans*i)%(10**9+7)
    return ans

def comb(n,r):
    return fact(n)*modpow(fact(r),10**9+5)*modpow(fact(n-r),10**9+5)%(10**9+7)

x,y=map(int,input().split(' '))
if (x+y)%3!=0 or 2*x-y<0 or 2*y-x<0:
    print(0)
else:
    x,y=max(x,y),min(x,y)
    d=x-y
    n=((x-2*d)//3)
    m=n+d
    print(comb(n+m,n))