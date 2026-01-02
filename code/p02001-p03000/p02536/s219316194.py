n,m=map(int,input().split())
#Union-Find木
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

#連結成分の個数を返す
def count():
  check=set()
  for i in range(n):
    parent=find(i)
    if parent not in check:
      check.add(parent)
  return len(check)

for i in range(m):
  a,b=map(int,input().split())
  unite(a-1,b-1)
s=count()
print(s-1)
    
  
