N, M = map(int, input().split())

par = list(range(0, N + 1))
size = [1] * (N + 1)
rank = [1] * (N + 1)

def root(i):
  if par[i] == i:
    return i
  else:
    par[i] = root(par[i])
    return par[i]
  
def same(i, j):
  return root(i) == root(j)
  
def findsize(i):
  size[i] = size[root(i)]
  
def unite(i, j):
  i = root(i)
  j = root(j)
  if i != j:
    if rank[i] > rank[j]:
      par[j] = i
      size[i] += size[j]
    else:
      par[i] = j
      size[j] += size[i]
      if rank[i] == rank[j]:
        rank[j] += 1

bridge = [None] * M
for i in range(M):
  x, y = map(int, input().split())
  bridge[i] = [x, y]
  
cnt = N * (N - 1) // 2
inconv = [0] * M
for i in range(M - 1, -1, -1):
  inconv[i] = cnt
  a, b = bridge[i]
  if not same(a, b):
    cnt -= size[root(a)] * size[root(b)]
    unite(a, b)
    
for i in range(M):
  print(inconv[i])