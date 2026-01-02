N, M = map(int, input().split())

edges = []
for _ in range(M):
  a, b = map(int, input().split())
  edges.append((a-1, b-1))
edges = edges[::-1]

# Union-Find
parent = [i for i in range(N)]
rank = [1] * (N)
count = [1] * (N)
def get_root(node):
  global parent
  if parent[node] == node:
    return node
  root = get_root(parent[node])
  parent[node] = root
  return root

def is_group(a, b):
  return get_root(a) == get_root(b)

def get_count(a):
  global count
  return count[get_root(a)]

def union(a, b):
  global rank
  root_a = get_root(a)
  rank_a = rank[root_a]
  root_b = get_root(b)
  rank_b = rank[root_b]
  if rank_a < rank_b:
    parent[root_a] = root_b
    count[root_b] += count[root_a]
  else:
    parent[root_b] = root_a
    count[root_a] += count[root_b]
    if rank_a == rank_b:
      rank[root_a] += 1

ans = [N * (N-1) // 2]
for f, t in edges[:-1]:
  if is_group(f, t):
    ans.append(ans[-1])
  else:
    ans.append(ans[-1] - get_count(f) * get_count(t))
    union(f, t)

for a in ans[::-1]:
  print(a)