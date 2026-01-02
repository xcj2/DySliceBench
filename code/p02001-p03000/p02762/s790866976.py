N,M,K=map(int,input().split())

par=[-1]*N
num=[0]*N

def find(x):
    if par[x-1]<0:
        return x
    else:
        par[x-1]=find(par[x-1])
        return par[x-1]

def union(x,y):
    p,q=find(x),find(y)
    if p==q:
        return
    if p>q:
        p,q=q,p
    par[p-1]+=par[q-1]
    par[q-1]=p   

def size(x):
    return -par[find(x)-1]

def same(x,y):
    return find(x)==find(y)
        

for _ in range(M):
    a,b=map(int,input().split())
    union(a,b)
    num[a-1]+=1
    num[b-1]+=1

for _ in range(K):
    c,d=map(int,input().split())
    if same(c,d):
        num[c-1]+=1
        num[d-1]+=1

for i in range(N):
    print(size(i+1)-1-num[i],end=" ")