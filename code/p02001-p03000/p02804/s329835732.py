def modpow(x,p,mod):
    ret=1
    for i in range(64):
        if (1<<i)&p:
            ret=ret*x%mod
        x=x*x%mod
    return ret

def inverse_table(n,mod):
    table=[]
    for i in range(0,n+1):
        table.append(modpow(i,mod-2,mod))
    return table

def factorial_table(n,mod):
    table=[1]
    for i in range(1,n+1):
        table.append(table[-1]*i%mod)
    return table

def inverse_factorial_table(n,it,mod):
    table=[1]
    for i in range(1,n+1):
        table.append(table[-1]*it[i]%mod)
    return table

it=inverse_table(10**5,1000000007)
ft=factorial_table(10**5,1000000007)
ift=inverse_factorial_table(10**5,it,1000000007)
def c(n,k,it,ft,mod):
    return ft[n]*ift[k]*ift[(n-k)]%mod
n,k=map(int,input().split())
a=sorted(map(int,input().split()))
hoge=[]
while True:
    hoge.append(c(n-1,k-1,it,ft,1000000007))
    if n-1==k-1:
        break
    n-=1
ans=0
for i in range(len(hoge)):
    ans-=hoge[i]*a[i]%1000000007
    ans+=hoge[i]*a[-i-1]%1000000007
    ans%=1000000007
print(ans)

