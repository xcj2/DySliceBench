N,M=map(int,input().split())

from collections import Counter
 
def soinsuu(n):
    list_=[]
    while(n!=1):
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                list_.append(i)
                n=n//i
                break
        else:
            list_.append(n)
            n=1
    return sorted(list_)
 
def product(a):
    pro=1
    for b in a:
        pro=pro*b%(10**9+7)
    return pro
 
#n!,nPr,nCrの高速計算
def n_func(n,mod=10**9+7):
    ans=1
    for i in range(1,n+1):
        ans=(ans*i)%mod
    return ans
def inv_n(n,mod=10**9+7):
    return pow(n,mod-2,mod)
def nPr(n,r,mod=10**9+7):
    ans=n_func(n-r,mod)
    ans=inv_n(ans,mod)
    return ans*n_func(n,mod)%mod
def nCr(n,r,mod=10**9+7):
    ans=n_func(n-r,mod)*n_func(r,mod)%mod
    ans=inv_n(ans,mod)
    return ans*n_func(n,mod)%mod
    
p=list(Counter(soinsuu(M)).values())
print(product([nCr(N+p[i]-1,p[i]) for i in range(len(p))]))