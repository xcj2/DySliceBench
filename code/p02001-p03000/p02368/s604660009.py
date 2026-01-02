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

def search_strongly_connection(v, visited, reverse_edges, parent, num):
  visited[v] = True
  for to in reverse_edges[v]:
    if not visited[to]:
      parent[to] = num
      search_strongly_connection(to, visited, reverse_edges, parent, num)

def main():
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
      search_strongly_connection(v, visited, reverse_edges, parent, v)
  
  q_num = int(input())
  for _ in range(q_num):
    u, v = map(int, input().split())
    print(1 if parent[u] == parent[v] else 0)

main()
