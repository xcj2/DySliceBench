import sys
n,m=map(int,input().split())
bridge=[[i for i in map(int,l.split())] for l in sys.stdin]
bridge.reverse()
all=(n*(n-1))//2
ans=[all]
root=[i for i in range(n+1)]
rank=[0]*(n+1)
size=[1]*(n+1)
def find(x):
  if root[x]==x:
    return x
  else:
    root[x]=find(root[x])
    return root[x]
def check(x,y):
  return find(x)==find(y)
def union(x,y):
  x=find(x)
  y=find(y)
  if rank[x]<rank[y]:
    root[x]=y
    size[y]+=size[x]
  else:
    root[y]=x
    size[x]+=size[y]
  if rank[x]==rank[y]:
    rank[x]+=1
for i in bridge:
  if check(i[0],i[1]):
    ans.append(ans[-1])
  else:
    ans.append(ans[-1]-size[find(i[0])]*size[find(i[1])])
    union(i[0],i[1])
ans.pop()
for i in range(m):
  print(ans.pop())