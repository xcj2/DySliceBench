import math
import sys

m=10**9 + 7 
sys.setrecursionlimit(1000010)
(N, u, v ) = list(map(int,input().split()))
A=[]
B=[]
D=[] 
INF = 10 ** 10

for i in range(0,N-1):
    (a, b) =  list(map(int,input().split()))
    A.append(a)
    B.append(b)
    
C=[[] for _ in range(N)]
# print(N,u,v, A, B, C) 

for i in range(0,N-1):
    # print(i,A[i],B[i])
    C[A[i]-1].append(B[i])
    C[B[i]-1].append(A[i])

def initD():
    global D
    D=[INF for _ in range(N)]
    
def dist(n):
    global D
    initD()
    D[n-1] = 0 
    for x in C[n-1]:
        # print("x1:",x)
        if D[x-1] == INF:
            distR(x,1)
    
def distR(n,d):
    global D
    D[n-1] = d
    for x in C[n-1]:
        if D[x-1] == INF:
            # print("x1,x2:",n,x)
            distR(x,d+1)


# print(N,u,v, A, B, C) 
dist(u)
U = D 
dist(v)
V = D
# print(U,V)

max = 0

for i in range(0,N):
    if U[i] < V[i]:
        if (V[i] - U[i]) % 2 ==0:
            x = V[i] - 1
        else:
            x = V[i] - 1
    
        if x > max:
            max = x
 
print(max) 