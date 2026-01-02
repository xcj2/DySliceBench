n,a,b=map(int,input().split())

mod=10**9+7
def cal(n):
    if n==1:
        return 2
    else:
        if n%2==0:
            return (cal(n//2)**2)%mod
        elif n%2!=0:
            return ((cal(n//2)*cal(n-n//2))%mod)
J=cal(n)-1
def find_power(n,mod):
    # 0!からn!までのびっくりを出してくれる関数(ただし、modで割った値に対してである）
    powlist=[0]*(n+1)
    powlist[0]=1
    powlist[1]=1
    for i in range(2,n+1):
        powlist[i]=powlist[i-1]*i%(mod)
    return powlist

def find_inv_power(n):
    #0!からn!までの逆元を素数10**9+7で割ったあまりリストを作る関数
    powlist=find_power(n,10**9+7)
    check=powlist[-1]
    first=1
    uselist=[0]*(n+1)
    secondlist=[0]*30
    secondlist[0]=check
    secondlist[1]=check**2
    for i in range(28):
        secondlist[i+2]=(secondlist[i+1]**2)%(10**9+7)
    a=format(10**9+5,"b")
    for j in range(30):
        if a[29-j]=="1":
            first=(first*secondlist[j])%(10**9+7)
    uselist[n]=first
    for i in range(n,0,-1):
        uselist[i-1]=(uselist[i]*i)%(10**9+7)
    return uselist

C=find_inv_power(2*10**5+100)
if  True:
    c=1
    for i in range(a):
        c*=(n-i)
        c=c%mod
    c=c*C[a]
    c=c%mod
    d=1
    for i in range(b):
        d*=(n-i)
        d=d%mod
    d=d%mod
    d=d*C[b]
    print((J-c-d)%mod)