# nCkの計算するやつ
# (n!)/(k!(n-k)!) mod p
# (n!) * (k!)^-1 * ((n-k)!)^-1 mod p

def comInit(MOD, n):
    fact=[1,1] # fact[n]はnの階乗
    invr=[0,1] # invr[n]はnの逆元
    invr_fact=[1,1] # invr_fact[n]は逆元の階乗

    for i in range(2,n+1):
        fact.append(fact[-1]*i%MOD)
        invr.append(-invr[MOD%i]*(MOD//i)%MOD)
        invr_fact.append(invr_fact[-1]*invr[-1]%MOD)
    return fact,invr_fact

def calCom(n,k,MOD,fact,invr_fact):
    k=min(k,n-k)
    return fact[n]*invr_fact[k]*invr_fact[n-k]%MOD

def main():
    x,y=map(int,input().split())

    if (x+y)%3!=0:
        print(0)
        return

    temp=int((x+y)/3)
    if temp*2 < x or temp > x:
        print(0)
        return
    f,inf=comInit(10**9+7,temp)
    # n,kはしっかりはっきりさせよ明日

    # ans=factorial(temp) / factorial(x-temp) / factorial(2*temp-x)
    ans=calCom(temp,abs(x-temp),10**9+7,f,inf)

    print(ans)

if __name__ == '__main__':
    main()
