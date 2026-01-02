
n, q = map(int, input().split())

p = [i for i in range(n)]
rank = [0 for i in range(n)]

def makeSet(x):
 p[x] = x
 rank[x] = 0

def union(x, y):
 link(findSet(x), findSet(y))

def link(x, y):
 if rank[x] > rank[y]:
  p[y] = x
 else:
  p[x] = y
  if rank[x] == rank[y]:
   rank[y] = rank[y] + 1

def findSet(x):
 if x != p[x]:
  p[x] = findSet(p[x])
 return p[x]


def unite(x, y):
 union(x, y)

def same(x, y):
 x = findSet(x)
 y = findSet(y)

 if x == y:
  return 1
 else :
  return 0


output = []

for i in range(q):
 com, x, y = map(int, input().split())

 if com == 0:
  unite(x, y)
 else :
  output.append(same(x,y))

for ans in output:
 print(ans)
