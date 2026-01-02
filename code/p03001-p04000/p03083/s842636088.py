mod=10**9+7
def gcd(x,y):
    if x<y:
        x,y=y,x
    #x>y
    if x%y==0:
        return y
    else:
        return gcd(y,x%y)
def egcd(a, b):
    (x,lastx)=(0,1)
    (y,lasty)=(1,0)
    while b != 0:
        q = a // b
        (a, b) = (b, a % b)
        (x, lastx) = (lastx - q * x, x)
        (y, lasty) = (lasty - q * y, y)
    return (lastx, lasty, a)
def inv(x):
    return egcd(x,mod)[0]%mod
N=2*10**5+10
B,W=map(int,input().split())
Blist=[0 for i in range(N+1)]
Wlist=[0 for i in range(N+1)]
Fact=[0 for i in range(N+1)]
Finv=[0 for i in range(N+1)]
Exp2=[0 for i in range(N+1)]
Fact[0]=1;Finv[0]=1
Exp2[0]=1
for i in range(N):
    Exp2[i+1]=(Exp2[i]*2)%mod
for i in range(N):
    Fact[i+1]=(Fact[i]*(i+1))%mod
    Finv[i+1]=inv(Fact[i+1])
def C(n,k):
    if k<0 or n<k:
        return 0
    else:
        return (Finv[k]*(Fact[n]*Finv[n-k])%mod)%mod
Blist[0]=1;Wlist[0]=1
for i in range(N):
    Blist[i+1]=(2*Blist[i]-C(i,B-1))%mod
    Wlist[i+1]=(2*Wlist[i]-C(i,W-1))%mod
#print(Blist[:B+W])
#print(Wlist[:B+W])
ans=[0 for i in range(B+W)]
for i in range(B+W):
    ans[i]=(Blist[i]-Wlist[i]+Exp2[i])%mod
    ans[i]=(ans[i]*inv(Exp2[i+1]))%mod
for line in ans:
    print(line)
