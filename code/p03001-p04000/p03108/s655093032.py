#120_D
#Union-Find
n,m=map(int,input().split())
edges=[]
for _ in range(m):
    a,b=map(int,input().split())
    edges.append((a-1,b-1))
edges=edges[::-1]

par=[i for i in range(n)]
size=[1 for _ in range(n)]
rank=[0 for _ in range(n)]

def find(x):#木の根を求める
    if par[x]==x:
        return x
    else:
        par[x]=find(par[x])
        return par[x]
    
def merge(x,y):#併合
    x=find(x)
    y=find(y)
    if x==y:
        return
    if rank[x]>rank[y]:
        par[y]=x
        size[x]+=size[y]
    else:
        par[x]=y
        size[y]+=size[x]
        if rank[x]==rank[y]:
            rank[y]+=1
            
def same(x,y):
    return find(x)==find(y)
    

ans=[n*(n-1)//2 for i in range(m)]
for i in range(0,m-1):
    a,b=edges[i]
    ans[i+1]=ans[i]
    if not same(a,b):
        ans[i+1]-=size[find(a)]*size[find(b)]
        merge(a,b)
        

ans=ans[::-1]
for i in range(m):
    print(ans[i])