#!/usr/bin/python3
# -*- coding:utf-8 -*-

from collections import defaultdict
from queue import deque

def main():
  n = int(input())
  graph = defaultdict(list)
  
  def is_bt():
    def bfs():
      colors = [-1] * len(graph)
      dq = deque()
      dq.append(0)
      colors[0] = 0
      while dq:
        inode = dq.popleft()
        for ichild in graph[inode]:
          if colors[ichild] == -1:
            colors[ichild] = abs(colors[inode]-1)
            dq.append(ichild)
          else:
            if colors[ichild] == colors[inode]:
              return False
      return True
    return bfs()
  
  def wf(edges):
    dp = edges
    for k in range(len(graph)):
      for i in range(len(graph)):
        for j in range(len(graph)):
          dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
    return dp
  
  edges = [[n+1] * n for _ in range(n)]  
  for i in range(n):
    for j, c in enumerate(input().strip()):
      if c == '1':
        graph[i].append(j)
        edges[i][j] = 1
    edges[i][i] = 0
  graph = dict(graph)
    
  if not is_bt():
    print(-1)
    return
  print(max([max(x) for x in wf(edges)]) + 1)
  
if __name__=='__main__':
  main()

