inf=10**17

def tp(a,b):
    return min(a,b,inf)
def tt(a,b):
    return min(a+b,inf)
def tpdot(A,B):#N正方行列のみにかけ算を許す
    N=len(A)
    C=[[inf]*N for i in range(N)]
    for i in range(N):
        for j in range(N):
            num=inf
            for k in range(N):
                t=tt(A[i][k],B[k][j])
                num=tp(num,t)
            C[i][j]=num
    return C
def tpeye(N):
    C=[[inf]*N for i in range(N)]
    for i in range(N):
        C[i][i]=0
    return C
def tppower(A,k):
    N=len(A)
    S,T=tpeye(N),A
    x=k
    while x>0:
        if x%2==1:
            S=tpdot(S,T)
        x=x//2
        T=tpdot(T,T)
    return S

H,W=map(int,input().split())
A=[[0]*10 for i in range(10)]
for j in range(10):
    C=[int(i) for i in input().split()]
    for k in range(10):
        A[j][k]=C[k]
#print(A)
A=tppower(A,10)
ans=0
for j in range(H):
    C=[int(i) for i in input().split()]
    for k in range(W):
        if C[k]!=-1:
            ans+=A[C[k]][1]
#print(A)
print(ans)