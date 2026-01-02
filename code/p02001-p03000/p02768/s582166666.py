n,a,b=map(int,input().split())

mod=10**9+7

def repmod(n,m):
    if n==1:return 2
    nn = n // 2
    te = repmod(nn, m)
    if n%2==0:
        ans=(te*te)%mod
        return ans
    elif n%2==1:
        ans=(2*te*te)%mod
        return ans
def extgcd(a,b):
    a0,b0=a,b
    x0,y0=1,0
    x1,y1=0,1

    while b0!=0:
        q = a0 // b0
        r = a0 % b0

        a0,b0=b0,r
        temp=x1
        x0,x1=x1,x0-q*x1
        y0,y1=y1,y0-q*y1

    return a0,x0,y0

def mo(x,m):
    return (m+x%m)%m

def inv(a,m):
    g,x,y=extgcd(a,m)
    ans=mo(x,m)
    return ans

total=repmod(n,mod)-1

c=max(a,b)

temp=1
s=0
for i in range(c):
    temp=(temp*(n-i))%mod
    invi=inv(i+1,mod)
    temp=temp*invi
    if i+1==a:
        s+=temp
    if i+1==b:
        s+=temp

ans=(total-s)%mod
print(ans)