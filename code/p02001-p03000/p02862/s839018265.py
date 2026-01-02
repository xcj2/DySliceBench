def find_power(n):
    # 0!からn!までのびっくりを出してくれる関数
    powlist=[0]*(n+1)
    powlist[0]=1
    powlist[1]=1
    for i in range(2,n+1):
        powlist[i]=powlist[i-1]*i%(10**9+7)
    return powlist
def find_inv_power(n):
    #0!からn!までの逆元を10**9+7で割ったあまりリストを作る関数
    powlist=find_power(n)
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
def combi(a,b,n,r,mod):
    if n<r:
        return 0
    elif n>=r:
        return (a[n]*b[r]*b[n-r])%(mod)
x,y=map(int,input().split())
power=find_power(1000000)
invpower=find_inv_power(1000000)
if (2*x-y)%3==0 and (2*y-x)%3==0:
    if (2*x-y)>=0 and (2*y-x)>=0:
        a=(2*y-x)//3
        b=(2*x-y)//3
        print(combi(power,invpower,a+b,b,10**9+7))
    else:
        print(0)
else:
    print(0)
    