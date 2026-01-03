h,w,a,b = map(int, input().split())
def find_power(n,mod=10**9+7):
    powlist=[0]*(n+1)
    powlist[0]=1
    powlist[1]=1
    for i in range(2,n+1):
        powlist[i]=powlist[i-1]*i%(mod)
    return powlist
def find_inv_power(n):
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
mod = 10**9+7
p_lis=find_power(4*10**5+100,mod)
ip_lis=find_inv_power(4*10**5+100)

def comb(n,r,mod=10**9+7):
    if n<r:
        return 0
    elif n>=r:
        return (p_lis[n]*ip_lis[r]*ip_lis[n-r])%(mod)
ans=0
for i in range(h-a):
    pre=comb(i+b-1,i)
    post=comb(h+w-b-2-i,h-i-1)
    ans+=pre*post
    ans%=10**9+7
print(ans)