def root(x):
    if(par[x]==x):
        return x
    else:
        r=root(par[x])
        diff_weight[x]+=diff_weight[par[x]]
        par[x]=r
        return r

def weight(x):
    root(x)
    return diff_weight[x]

def diff(x,y):
    return weight(y)-weight(x)

def relate(a,b,w):
    w+=weight(a);w-=weight(b)
    a=root(a)
    b=root(b)
    if(a==b):
        return False
    if rank[a]<rank[b]:
        a,b=b,a
        w=-w
    if rank[a]==rank[b]:
        rank[b]+=1
        par[b]=a
    par[b]=a
    diff_weight[b]=w
    siz[a]+=siz[b]
    return True

def size(a):
    return siz[root(a)]
    
def same(a,b):
    return root(a)==root(b)
    
N,Q=map(int,input().split())
par=[i for i in range(N)]
siz=[1 for _ in range(N)]
rank=[0 for _ in range(N)]
diff_weight=[0 for _ in range(N)]
for i in range(Q):
    query=list(map(int,input().split()))
    if not query[0]:
        X,Y,W=query[1:]
        relate(X,Y,W)
    else:
        X,Y=query[1:]
        if same(X,Y):
            print(diff(X,Y))
        else:
            print('?')
