N,K=map(int,input().split())
p=[int(i)-1 for i in input().split()]
q=[int(i)-1 for i in input().split()]
e=[i for i in range(N)]
def cir(x,y):
    z=[0]*N
    for i in range(N):
        z[i]=x[y[i]]
    return z
def inv(x):
    z=[0]*N
    for i in range(N):
        z[x[i]]=i
    return z
def f(x,y):
    return cir(y,inv(x))

def double(x,k):
    a=k
    t=x
    num=e
    while a!=0:
        if a%2==1:
            num=cir(num,t)
        a=a//2
        t=cir(t,t)
    return num
P=inv(p)
Q=inv(q)
#print(p,q,P,Q)
quo=(K-1)//6
r=K-quo*6-1
X=cir(q,cir(P,cir(Q,p)))
#Y=cir(P,cir(q,cir(p,Q)))
#Z=cir(q,double(Y,quo))
Z=double(X,quo)
A=cir(Z,cir(p,inv(Z)))
B=cir(Z,cir(q,inv(Z)))
#print(A,B,quo,r)
def g(n):
    if n==0:
        return A
    if n==1:
        return B
    return f(g(n-2),g(n-1))
L=g(r)
for i in range(N):
    L[i]+=1
print(' '.join(map(str,L)))
