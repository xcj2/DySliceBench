N,M=list(map(int,input().split()))
g=[list(map(int,input().split())) for _ in range(M)]

par=[0]*(N+1)

def find(x):
    if x==par[x]:
        return x
    else:
        par[x]=find(par[x])
        return par[x]

def same(x,y):
    return find(x)==find(y)

def unite(x,y):
    x=find(x)
    y=find(y)

    if x==y:
        return
    
    par[y]=x

ret=0

for i in range(M):
    par=list(range(N+1))

    for j in range(M):
        if i==j:
            continue
        a,b=g[j]

        unite(a,b)
    
    for j in range(1,N+1):
        if not same(1,j):
            ret+=1
            break
    

print(ret)