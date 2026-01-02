
# input V, E
v, e = map(int, input().split())


# input weighted edges into priority queue
import heapq
h = []
for i in range(e):
	s, t, w = map(int, input().split())
	heapq.heappush(h, (w, s, t))


# initialize union find tree for vertices
p = [i for i in range(v)]
rank = [0 for i in range(v)]

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
  return True
 else :
  return False


# search MST
s = 0
for i in range(e):
	edge = heapq.heappop(h)
	if same(edge[1], edge[2]) == False:
		s = s + edge[0]
		unite(edge[1], edge[2])

# print sum of weights
print(s)
