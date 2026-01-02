N, M = map(int, input().split())
X = [tuple(map(int, input().split())) for _ in range(M)]
X.reverse()

# Union Find
parent = [-1 for _ in range(N)]
rank = [0 for _ in range(N)]
def find(x):
  #print(x, parent[x])
  if parent[x] < 0:
    return x
  else:
    p = find(parent[x]) 
    parent[x] = p
    return p
  
def merge(x, y):
  a = find(x)
  b = find(y)
  if a == b:
    return False
  if rank[a] < rank[b]:
    a, b = b, a
  parent[a] += parent[b]
  parent[b] = a
  rank[a] = max(rank[a], rank[b]+1)
  return True
  
def is_connected(a,b):
  return find(a) == find(b)

ans = [0 for _ in range(M+1)]
ans[0] = N*(N-1)//2
i = 1
for a, b in X:
  a -= 1
  b -= 1
  #print(i, a, b, find(a), find(b))
  if find(a) == find(b):
    ans[i] = ans[i-1]
  else:
    m = -parent[find(a)]
    n = -parent[find(b)]
    ans[i] = ans[i-1] + m*(m-1)//2 + n*(n-1)//2
    merge(a, b)
    l = -parent[find(a)]
    ans[i] -= l*(l-1)//2
    #print(i, m, n, l, a, b, parent[a], parent[b])
  i += 1

ans.pop()
ans.reverse()
print(*ans, sep = "\n")
  