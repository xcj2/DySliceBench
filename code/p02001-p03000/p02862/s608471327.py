from math import factorial
def com(n,k,mod,fac,infac):
    k=min(k,n-k)
    return fac[n]*infac[k]*infac[n-k]%mod

def cominit(mod,n):
    fac=[1,1]
    infac=[1,1]
    inv=[0,1]

    for i in range(2,n+1):
        fac.append(fac[-1]*i%mod)
        inv.append(-inv[mod%i]*(mod//i)%mod)
        infac.append(infac[-1]*inv[-1]%mod)

    return fac,infac
def main():
    x,y=map(int,input().split())

    if (x+y)%3!=0:
        print(0)
        return

    temp=int((x+y)/3)
    if temp*2 < x or temp > x:
        print(0)
        return
    f,inf=cominit(10**9+7,temp)
    # n,kはしっかりはっきりさせよ明日

    # ans=factorial(temp) / factorial(x-temp) / factorial(2*temp-x)
    ans=com(temp,abs(x-temp),10**9+7,f,inf)

    print(ans)

if __name__ == '__main__':
    main()
