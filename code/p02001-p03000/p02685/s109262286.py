mod=998244353


##mod,nについての制約は自分でいかに記入する

def find_power(n,mod):
    # 0!からn!までのびっくりを出してくれる関数(ただし、modで割った値に対してである）
    powlist=[0]*(n+1)
    powlist[0]=1
    powlist[1]=1
    for i in range(2,n+1):
        powlist[i]=powlist[i-1]*i%(mod)
    return powlist

def find_inv_power(n,mod):
    #0!からn!までの逆元を素数modで割ったあまりリストを作る関数
    c=1
    uselist=[0 for i in range(n+1)]
    for i in range(1,n+1):
        c*=i
        c%=mod
    first=pow(c,mod-2,mod)
    uselist[n]=first
    for i in range(n,0,-1):
        uselist[i-1]=(uselist[i]*i)%(mod)
    return uselist
    
A=find_power(4*10**5,mod)
B=find_inv_power(4*10**5,mod)

def combi(n,r,mod):
    if n<r:
        return 0
    elif n>=r:
        return (A[n]*B[r]*B[n-r])%(mod)



N,M,K=map(int,input().split())
dp=[0 for i in range(N+1)]
#dp[x]=塗り方でダブりが、ｘ通りになるものの個数
ans=M*pow(M-1,N-1,mod)

for i in range(1,K+1):
    ans+=M*combi(N-1,i,mod)*pow(M-1,N-1-i,mod)
print(ans%mod)
