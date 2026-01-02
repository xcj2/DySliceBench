import math
N,M=map(int,input().split())
def primecheck(K):
    A=int(math.sqrt(K))+1
    for i in range(2,A+1):
        if K%i==0:
            return i
    return 1
D=dict()
while(True):
    X=int(math.sqrt(M))+1
    for i in range(2,X+1):
        if M%i==0:
            while(True):
                if i in D:
                    D[i]+=1
                else:
                    D[i]=1
                M=M//i
                if M%i!=0:
                    break
    j=primecheck(M)
    if j==1:
        if M==1:
            break
        D[M]=1
        break
    else:
        if j in D:
            D[j]=1
        else:
            D[j]+=1
P=10**9+7
def egcd(a, b):
    (x, lastx) = (0, 1)
    (y, lasty) = (1, 0)
    while b != 0:
        q = a // b
        (a, b) = (b, a % b)
        (x, lastx) = (lastx - q * x, x)
        (y, lasty) = (lasty - q * y, y)
    return (lastx, lasty, a)
def inv(x):
    return egcd(x,P)[0]
Y=2*10**5
Fact=[0 for i in range(Y+1)]
Finv=[0 for i in range(Y+1)]
Fact[0]=1
Finv[0]=1
for i in range(Y):
    Fact[i+1]=(Fact[i]*(i+1))%P
    Finv[i+1]=inv(Fact[i+1])%P
def C(n,k):
    return (Fact[n]*(Finv[k]*Finv[n-k])%P)%P
ans=1
for p in D:
    e=D[p]
    ans=ans*C(e+N-1,N-1)
    ans=ans%P
print(ans)
