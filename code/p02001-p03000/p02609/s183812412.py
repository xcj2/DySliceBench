from collections import deque
LIM=200004
L=[0]*LIM

def bin_sum(Y):
    S=bin(Y)[2:]
    count=0
    for i in range(len(S)):
        count+=int(S[i])
    return count

def bin_sum2(Y):
    count=0
    for i in range(len(Y)):
        count+=int(Y[i])
    return count

for i in range(1,LIM):
    L[i]+=bin_sum(i)

def pop_num(N,b,L):
    if N==0:
        return 0
    v=N%b
    return pop_num(v,L[v],L)+1
    
M=[0]*200005
for i in range(1,200004):
    M[i]+=pop_num(i,L[i],L)
X=int(input())
Y=input()
d=bin_sum2(Y)
e=int(Y,2)%(d+1)
f=int(Y,2)%max(1,(d-1))
O=[1]*(X+2)
P=[1]*(X+2)
q=max(d-1,1)
for i in range(1,X+1):
    O[i]=O[i-1]*2%q
    P[i]=P[i-1]*2%(d+1)
for i in range(X):
    
    if int(Y[i])==1:
        b=max(d-1,1)
        flag=max(0,d-1)
        g=(f-O[X-1-i]+b)%b
    else:
        b=d+1
        flag=1
        g=(e+P[X-1-i])%b

    if flag==0:
        print(0)
    elif g==0:
        print(1)
    else:
        print(M[g]+1)