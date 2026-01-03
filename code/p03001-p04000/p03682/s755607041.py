n=int(input())
xy=[]
for i in range(n):
  xy.append(list(map(int,input().split()))+[i])
  
x_sort=sorted(xy,key=lambda x:x[0])
y_sort=sorted(xy,key=lambda x:x[1])
edge=[]
for i in range(1,n):
  edge.append([min(abs(x_sort[i][1]-x_sort[i-1][1]),abs(x_sort[i][0]-x_sort[i-1][0])),x_sort[i][2],x_sort[i-1][2]])
  edge.append([min(abs(y_sort[i][1]-y_sort[i-1][1]),abs(y_sort[i][0]-y_sort[i-1][0])),y_sort[i][2],y_sort[i-1][2]])
edge.sort(key=lambda x:x[0])


#Union-Find
par=[i for i in range(n)]
deep=[1 for i in range(n)]
size=[1 for i in range(n)]
def find(x):
  if par[x]==x:
    return x
  else:
    return find(par[x])

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

def same(x,y):
  return find(x)==find(y)

#クラスカル法
#n:頂点数　edge:重みでsortした辺のリスト
def kruskal(n,edge):
  res=0
  #w:重さ s:始点　t:終点
  for w,s,t in edge:
    if not same(s,t):
      unite(s,t)
      res+=w
  return res

#連結でコストが最小になるものを求める
#最小全域木

print(kruskal(n,edge))








  