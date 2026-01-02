import sys

sys.setrecursionlimit(1000000)

#dfs...orderに帰りがけ順の逆順を保存
def dfs(v, visited, edges, order):
  visited[v] = True
  for to in edges[v]:
    if not visited[to]:
      dfs(to, visited, edges, order)
  order.append(v)

#最初のノードを強連結成分の親にする
def search_strongly_connection(v, visited, reverse_edges, parent, num):
  visited[v] = True
  for to in reverse_edges[v]:
    if not visited[to]:
      parent[to] = num
      search_strongly_connection(to, visited, reverse_edges, parent, num)

def main():
  #input
  v_num , e_num = map(int, input().split())
  edges = [[] for _ in range(v_num)]
  reverse_edges = [[] for _ in range(v_num)]
  for _ in range(e_num):
    s, t = map(int, input().split())
    edges[s].append(t)
    reverse_edges[t].append(s)
  
  #帰りがけ順の取得
  order = []
  visited = [False] * v_num
  for v in range(v_num):
    if not visited[v]:
      dfs(v, visited, edges, order)
  order.reverse()
  
  #強連結の探索
  visited = [False] * v_num
  parent = [i for i in range(v_num)]
  for v in order:
    if not visited[v]:
      search_strongly_connection(v, visited, reverse_edges, parent, v)
  
  #output
  for i in range(v_num):
    if parent[i] != i:
      print(1)
      break
  else:
    print(0)
main()
