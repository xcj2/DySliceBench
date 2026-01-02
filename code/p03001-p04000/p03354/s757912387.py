#097_D
n, m = map(int, input().split())
p = [int(x)-1 for x in input().split()]

#Union-Find
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

for _ in range(m):
    x, y = map(int, input().split())
    x, y = x-1, y-1
    merge(x, y)

ans = 0
for i in range(n):
    if same(i, p[i]):
        ans += 1
        
print(ans)