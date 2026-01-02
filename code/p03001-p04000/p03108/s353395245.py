n, m = map(int, input().split())
par = [i for i in range(n)]
rank = [1] * n
size = [1] * n


ab = []
for i in range(m):
  a, b = map(int, input().split())
  a -= 1
  b -= 1
  ab.append([a,b])
'''
ab = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]
'''
def find(x):
  if par[x] == x:
    return x
  else:
    return find(par[x])

def same(x, y):
  return find(x) == find(y)

def union(x, y):
  x = find(x)
  y = find(y)
  if x != y:
    if rank[x] < rank[y]:
      par[x] = y
      size[y] += size[x]
    else:
      par[y] = x
      size[x] += size[y]
      if rank[x] == rank[y]:
        rank[x] += 1


ans = [0 for i in range(m)]
# print (par,size,rank)
for i in range(m-1, -1, -1):
  x = find(ab[i][0])
  y = find(ab[i][1])
  if x != y:
    ans[i] = size[x] * size[y]
    union(x,y)
  # print(par,size,rank)
'''
print (ans)
print (par)
print (size)
print (rank)
'''
s = 0
for i in ans:
  s += i
  print (s)
