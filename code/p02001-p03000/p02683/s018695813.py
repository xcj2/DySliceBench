import math

def to_binary(n,N):
    B=[]
    for i in range(N):
        B=[n%2]+B
        n//=2

    return B

def list_sum(A,N,M,L):
    U=[0 for j in range(M)]
    
    for i in range(N):
        if L[i]==1:
            for j in range(M):
                U[j]+=A[i][j]
    return U

def inner(A,B):
    n=len(A)
    S=0
    for i in range(n):
        S+=A[i]*B[i]
    return S

N,M,X=map(int,input().split())
C=[]
A=[]

for i in range(N):
    T=list(map(int,input().split()))
    C.append(T[0])
    A.append(T[1:])

J=math.inf
for i in range(2**N):
    L=to_binary(i,N)
    U=list_sum(A,N,M,L)
    if min(U)>=X:
        J=min(J,inner(C,L))

if J==math.inf:
    print(-1)
else:
    print(J)
    
