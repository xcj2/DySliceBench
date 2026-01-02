#!/usr/bin/python3
# -*- coding: utf-8 -*-
from collections import defaultdict,deque


class Graph:

  def __init__(self,N,uv,S,T):
    self.graph = uv
    self.start = S
    self.goal = T
    self.states  = [[-3 for _ in range(3)] for _ in range(N)]
    self.states[self.start][0] = 0

  def solve(self):
    nxt = deque([self.start])
    ## update
    while len(nxt) > 0:
      p = nxt.popleft()
      for q in self.graph[p]:
        for ps in range(3):
          if self.states[p][ps] >= 0:
            qs = (ps+1)%3
            if self.states[q][qs] < 0:
              self.states[q][qs] = self.states[p][ps]+1
              nxt.append(q)
            else:
              self.states[q][qs] = min(self.states[q][qs],self.states[p][ps]+1)
    ## return
    return self.states[self.goal][0]


def main():
  ## input
  N,M = map(int, input().split())
  uv = defaultdict(set)
  for _ in range(M):
    u,v = map(int, input().split())
    uv[u-1].add(v-1)
  S,T = map(int, input().split())

  ## solve
  graph = Graph(N,uv,S-1,T-1)
  print(graph.solve()//3)


if __name__ == "__main__":
  main()