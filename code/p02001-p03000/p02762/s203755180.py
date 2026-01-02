n,m,k=map(int,input().split())
#par[i]:iの親　deep[i]:iの深さ　size[i]:iの大きさ
par=[i for i in range(n)]
deep=[1]*n
size=[1]*n

#親を見つける
def find(x):
  if par[x]==x:
    return x
  else:
    return find(par[x])

#二つのグループを統合する
def unite(x,y):
  x=find(x)
  y=find(y)
  if x==y:
    return
  if deep[x]<deep[y]:
    par[x]=y
    size[y]+=size[x]
  else:
    par[y]=x
    size[x]+=size[y]
    if deep[x]==deep[y]:
      deep[x]+=1

#xとyが同じグループに属するかどうか
def same(x,y):
  return find(x)==find(y)

#xが属するグループの要素数を返す
def group_count(x):
  return size[find(x)]





es=[[] for i in range(n)]
for i in range(m):
  a,b=map(int,input().split())
  es[a-1].append(b)
  es[b-1].append(a)
  unite(a-1,b-1)

cnt=[1]*n
for i in range(n):
  cnt[i]=group_count(i)
  
check=[0]*n
for j in range(k):
  c,d=map(int,input().split())
  if same(c-1,d-1):
    check[c-1]+=1
    check[d-1]+=1
for i in range(n):
  print(cnt[i]-1-len(es[i])-check[i],end=" ")
  
  
  
  
