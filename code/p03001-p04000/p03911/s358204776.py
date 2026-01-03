#CODE FES 2016 C
n, m = map(int, input().split())

par=[i for i in range(n+m)]
size=[1 for _ in range(n+m)]
rank=[0 for _ in range(n+m)]
 
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

for i in range(n):
    l = list(map(int, input().split()))[1:]
    for j in range(len(l)):
        merge(i, l[j]+n-1)
flg = True
for i in range(1, n):
    if not same(0, i):
        flg = False
print('YES' if flg else 'NO')