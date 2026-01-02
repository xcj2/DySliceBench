n,m=map(int,input().split())

parent=[i for i in range(n)]
rank=[0 for i in range(n)]

def find(a):
  if parent[a]==a:
    return a
  else:
    return find(parent[a])

def union(a,b):
  ar=find(a)
  br=find(b)
  if ar==br:
    return
  if rank[a]>rank[b]:
    parent[br]=ar
  else:
    parent[ar]=br
    if rank[a]==rank[b]:
      rank[a]+=1
      
def same(a,b):
  ar=find(a)
  br=find(b)
  return ar==br

q=[None]*m

for i in range(m):
  x,y,z=map(int,input().split())
  q[i]=[x-1,y-1]

for i in range(len(q)):
  union(q[i][0],q[i][1])
  
roots=[0]*len(parent)
for i in range(len(parent)):
  roots[i]=find(i)

print(len(set(roots)))
