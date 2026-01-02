n,m=map(int,input().split())
par=[i for i in range(n)] #親
rank=[1]*n #深さ
size=[1]*n #iを根とするグループのサイズ
#親を見つける
def find(x):
  if par[x]==x:
    return x
  else:
    return find(par[x])
  
#xの属するグループとyの属するグループを併合
def unite(x,y):
  x=find(x)
  y=find(y)
  if x==y:
    return
  if rank[x]<rank[y]:
    par[x]=y
    size[y]=size[y]+size[x]
  else:
    par[y]=x
    size[x]=size[x]+size[y]
    if rank[x]==rank[y]:
      rank[x]+=1
      
#xとyが同じグループに属するかどうか
def same(x,y):
  return find(x)==find(y)

#check=set()
for i in range(m):
  a,b=map(int,input().split())
  unite(a-1,b-1)
  
ans=0

for i in range(n):
  ans=max(ans,size[find(i)])
print(ans)

