#!/usr/bin/python3
# -*- coding:utf-8 -*-

import sys
sys.setrecursionlimit(10**8)

def main():
  n, m = map(int, input().split())
  tree = [[] for _ in range(n)]
  for im in range(m):
    a, b = map(int, input().split())
    tree[a-1].append(b-1)
    tree[b-1].append(a-1)
  
  def get_bridge(tree):
    bridge_targets = []
    n = len(tree)
    pres = [0 for _ in range(n)]
    lows = [0 for _ in range(n)]
    visited = [0 for _ in range(n)]
    used_edges = []
    def dfs(inode, count=0):
      pres[inode] = lows[inode] = count
      visited[inode] = 1
      for ichild in tree[inode]:
        if not visited[ichild]:
          used_edges.append((inode, ichild))
          count = dfs(ichild, count+1)
        if lows[ichild] < lows[inode]:
          if not (ichild, inode) in used_edges:
            lows[inode] = lows[ichild]
      if pres[inode] == lows[inode]:
        bridge_targets.append(inode)
      
      return count
    dfs(0)
    return [(s, t) for (s, t) in used_edges if t in bridge_targets]
  bridges = get_bridge(tree)
  print(len(bridges))
  
if __name__=='__main__':
  main()

