def extgcd(a,b):
    a0,b0=a,b
    x0,y0=1,0
    x1,y1=0,1

    while b0!=0:
        q = a0 // b0
        r = a0 % b0

        a0,b0=b0,r
        x0,x1=x1,x0-q*x1
        y0,y1=y1,y0-q*y1

    return a0,x0,y0

def mo(x,m):
    return (m+x%m)%m

def inv(a,m):
    g,x,y=extgcd(a,m)
    ans=mo(x,m)
    return ans

def combi_mod(n,k,m):
    mi=min(k,n-k)
    invlist = [1]
    for i in range(1, mi + 1):
        temp = inv(i, m)
        invlist.append(temp)
    ans=1

    for i in range(1,mi+1):
        ans=(ans*(n+1-i)*invlist[i])%m
    ans = ans % m
    return ans

X,Y=map(int,input().split())
mod=1000000007

if (2*Y-X)%3!=0 or (2*X-Y)%3!=0:
    print(0)
    exit()

a=(2*X-Y)//3
b=(2*Y-X)//3

if a<0 or b<0:
    print(0)
    exit()

ans=combi_mod(a+b,a,mod)
print(ans)

