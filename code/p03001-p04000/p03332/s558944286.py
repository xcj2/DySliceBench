P=998244353
MAX_N=3*10**5+1
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
Fact=[0 for i in range(MAX_N+1)]
Finv=[0 for i in range(MAX_N+1)]
Fact[0]=1
Finv[0]=1
for i in range(MAX_N):
    Fact[i+1]=(Fact[i]*(i+1))%P
    Finv[i+1]=inv(Fact[i+1])%P
def C(n,k):
    return (Fact[n]*(Finv[k]*Finv[n-k])%P)%P
N,A,B,K=map(int,input().split())
L=[]
for i in range(K//A+1):
    if (K-A*i)%B==0:
        j=(K-A*i)//B
        if 0<=i<=N and 0<=j<=N:
            L.append((i,j))
ans=0
for x,y in L:
    ans+=C(N,x)*C(N,y)
    ans%=P
print(ans)

