def find(x):
  if par[x] < 0:
    return x
  else:
    par[x] = find(par[x])
    return par[x]

def unite(x,y):
  x,y=find(x),find(y)
  if x!=y:
    if x>y:
        x,y=y,x
    par[x]+=par[y]
    par[y]=x

def same(x, y):
  return find(x) == find(y)

 
def size(x):
  return-par[find(x)]

n, m, k = map(int, input().split())

par = [-1]*n
FF = [0] * n
BB = [[] for i in range(n)]

for i in range(m):
  a, b = map(int, input().split())
  unite(a-1, b-1)
  FF[a-1] += 1
  FF[b-1] += 1
for i in range(k):
  a, b = map(int, input().split())
  BB[a-1].append(b-1)
  BB[b-1].append(a-1)
result = []

for i in range(n):
  ans = size(i) - FF[i] -1
  for j in BB[i]:
    if same(i, j):
      ans -= 1
  result.append(ans)
  
print(*result)