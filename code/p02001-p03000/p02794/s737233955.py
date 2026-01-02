import sys
input = sys.stdin.buffer.readline

N = int(input())
AB = [list(map(int, input().split())) for _ in range(N - 1)]
M = int(input())
UV = [list(map(int, input().split())) for _ in range(M)]

def popcnt(n):
    c = (n & 0x5555555555555555) + ((n >> 1) & 0x5555555555555555)
    c = (c & 0x3333333333333333) + ((c >> 2) & 0x3333333333333333)
    c = (c & 0x0f0f0f0f0f0f0f0f) + ((c >> 4) & 0x0f0f0f0f0f0f0f0f)
    c = (c & 0x00ff00ff00ff00ff) + ((c >> 8) & 0x00ff00ff00ff00ff)
    c = (c & 0x0000ffff0000ffff) + ((c >> 16) & 0x0000ffff0000ffff)
    c = (c & 0x00000000ffffffff) + ((c >> 32) & 0x00000000ffffffff)
    return c
    
graph = [[] for _ in range(N + 1)]
for a, b in AB:
  graph[a].append(b)
  graph[b].append(a)
  
def make_tree(graph, root) -> (list, list):
  INF = 10 ** 15
  dist = [INF] * len(graph)
  parent = [-1] * len(graph)
  stack = [root]
  dist[root] = 0
  parent[root] = root
  while stack:
    s = stack.pop()
    for g in graph[s]:
      if dist[g] > dist[s] + 1:
        dist[g] = dist[s] + 1
        parent[g] = s
        stack.append(g)
  return dist, parent
 
def lca(u, v, dist, parent):
  distu, distv = dist[u], dist[v]
  if distu > distv:
    for _ in range(distu - distv):
      u = parent[u]
  if distv > distu:
    for _ in range(distv - distu):
      v = parent[v]
  while u != v:
    u, v = parent[u], parent[v]
  return u

dist, parent = make_tree(graph, 1)

tree_lca = []
for i in range(M):
    tmp = 0
    u, v = UV[i]
    l = lca(u, v, dist, parent)
    while u != l:
        tmp |= 1 << u
        u = parent[u]
    while v != l:
        tmp |= 1 << v
        v = parent[v]
    tree_lca.append(tmp)

answer = 2 ** (N - 1)
for i in range(1, 2 ** M):
    tmp = 0
    for j in range(M):
        if (i >> j) & 1:
            tmp |= tree_lca[j]
    cnt = popcnt(tmp)

    if popcnt(i) % 2 == 1:
        answer -= 2 ** (N - 1 - cnt) 
    else:
        answer += 2 ** (N - 1 - cnt) 
        
print(answer)