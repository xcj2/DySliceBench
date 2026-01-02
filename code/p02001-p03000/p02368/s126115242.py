"""
強連結成分分解
"""

import sys

sys.setrecursionlimit(1000000)

def dfs(v, visited, edges, order):
  visited[v] = True
  for to in edges[v]:
    if not visited[to]:
      dfs(to, visited, edges, order)
  order.append(v)

def search_strongly_connection(v, visited, reverse_edges, parent):
  visited[v] = True
  for to in reverse_edges[v]:
    if not visited[to]:
      parent[to] = v
      search_strongly_connection(to, visited, reverse_edges, parent)

def find(parent, x):
  if parent[x] == x:
    return x
  tmp = find(parent, parent[x])
  parent[x] = tmp
  return tmp

v_num , e_num = map(int, input().split())
edges = [[] for _ in range(v_num)]
reverse_edges = [[] for _ in range(v_num)]
for _ in range(e_num):
  s, t = map(int, input().split())
  edges[s].append(t)
  reverse_edges[t].append(s)


order = []
visited = [False] * v_num
for v in range(v_num):
  if not visited[v]:
    dfs(v, visited, edges, order)
order.reverse()


visited = [False] * v_num
parent = [i for i in range(v_num)]
for v in order:
  if not visited[v]:
    search_strongly_connection(v, visited, reverse_edges, parent)

q_num = int(input())
for _ in range(q_num):
  u, v = map(int, input().split())
  if find(parent, u) == find(parent, v):
    print(1)
  else:
    print(0)
