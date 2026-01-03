n=int(input())
town=[]
for i in range(n):
  x,y=map(int,input().split())
  town.append([x,y,i])

  
X=sorted(town,key=lambda x:x[0])

Y=sorted(town,key=lambda x:x[1])
es=[]
for i in range(1,n):
  es.append((min(abs(X[i][0]-X[i-1][0]),abs(X[i][1]-X[i-1][1])),X[i][2],X[i-1][2]))
  es.append((min(abs(X[i][0]-X[i-1][0]),abs(X[i][1]-X[i-1][1])),X[i-1][2],X[i][2]))
  es.append((min(abs(Y[i][0]-Y[i-1][0]),abs(Y[i][1]-Y[i-1][1])),Y[i][2],Y[i-1][2]))
  es.append((min(abs(Y[i][0]-Y[i-1][0]),abs(Y[i][1]-Y[i-1][1])),Y[i-1][2],Y[i][2]))
es.sort(key=lambda x:x[0])


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
  
#クラスカル法
#esは重みで小さい順にsort済み
#es[i]:[重み、始点、終点]
def kruskal(n,es):
  ans=0
  for to in es:
    if not same(to[1],to[2]):
      ans+=to[0]
      unite(to[1],to[2])
  return ans

      
  
print(kruskal(n,es))
