# D　イロハちゃんと升目
cnt=0
h,w,a,b=map(int,input().split())
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

powlist=find_power(h+w+1)
invlist=find_inv_power(h+w+1)
def combi(n,r):
    a=powlist
    b=invlist
    if n<r:
        return 0
    elif n>=r:
        return (a[n]*b[r]*b[n-r])%(10**9+7)

for i in range(h-a):
    cnt+=(combi(b+i-1,i)*combi(w+h-2-b-i,h-1-i))%(10**9+7)
print(cnt%(10**9+7))
    
