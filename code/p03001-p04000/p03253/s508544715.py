n,m=map(int,input().split())
pem=1
if m==1:
    print(1)
def fctr2(n): #それぞれの素因数の指数だけ出力
    f=[]
    c=0
    r=int(n**0.5)
    for i in range(2,r+2):
        while n%i==0:
            c+=1
            n=n//i
        if c!=0:
            f.append(c)
            c=0
    if n!=1:
        f.append(1)
    return f

mod=10**9+7
fuc=[1]
def fucfun(n):
    for i in range(1,n):
        e=fuc[i-1]*i
        fuc.append(e%mod)
def com(n,k):
    com=(fuc[n]%mod)*pow(fuc[k],mod-2,mod)*pow(fuc[n-k],mod-2,mod)
    return com
f=fctr2(m)
if m!=1:
    a=max(f)+n
    fucfun(a)
    s=1
    for i in range(len(f)):
        t=com(f[i]+n-1,f[i])
        s=(s*t)%mod
    print(s)