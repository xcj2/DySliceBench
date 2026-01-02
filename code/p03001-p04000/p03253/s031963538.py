N,M=map(int,input().split())
mod=10**9+7
 
from math import factorial
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
        pro=pro*b%mod
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
    
nPr_list=[nPr(N,i) for i in range(30)]
bunbo_list=dict()

def dp(cur,init,seq,lest,num):
    #print(cur,init,seq,lest,num)
    if cur==N:
        if lest==0:
            cnt=sorted(list(Counter(seq).values())+[N-len(seq)],reverse=True)
            bunbo=product(map(factorial,cnt[1:]))
            if bunbo not in bunbo_list.keys():
                bunbo_list[bunbo]=inv_n(bunbo)
            memo[num]=(memo[num]+nPr_list[N-cnt[0]]*bunbo_list[bunbo])%mod
    elif lest==0:
        dp(N,init,seq,0,num)
    else:
        if cur==0:
            for i in range(1,lest+1):
                dp(cur+1,init,seq+[i],lest-i,num)
        else:
            for i in range(1,min(lest,seq[-1])+1):
                dp(cur+1,init,seq+[i],lest-i,num)
 
p=list(Counter(soinsuu(M)).values())
memo=[0]*len(p)


for i in range(len(p)):
    dp(0,p[i],[],p[i],i)
print(product(memo))