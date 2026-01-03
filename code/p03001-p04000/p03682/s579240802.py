import itertools
import heapq
from heapq import heappush, heappop
global G, inp_x, inp_y

def input_graph(N):
  global G, inp_x, inp_y
  inp_x = []
  inp_y = []
  for i in range(N):
    x, y = map(int, input().split())
    inp_x.append((x, i))
    inp_y.append((y, i))
  inp_x.sort()
  inp_y.sort()
  for i in range(N-1):
    xa = inp_x[i][1]
    xb = inp_x[i+1][1]
    ya = inp_y[i][1]
    yb = inp_y[i+1][1]
    cost_x = abs(inp_x[i][0]-inp_x[i+1][0])
    cost_y = abs(inp_y[i][0]-inp_y[i+1][0])
    G[xa] += [(cost_x, xb)]
    G[xb] += [(cost_x, xa)]
    G[ya] += [(cost_y, yb)]
    G[yb] += [(cost_y, ya)]

  
def prim(V):
  global G, used
  edgelist = []
  for e in G[0]:
    heappush(edgelist, e)
  used[0] = True
  res = 0
  while edgelist:
    minedge = heappop(edgelist)
    if used[minedge[1]]:
      continue 
    v = minedge[1]
    used[v] = True 
    for e in G[v]:
      if not used[e[1]]:
        heappush(edgelist, e)
    res += minedge[0]
  return res

def main():
  global G, used
  N = int(input())
  G = [[] for _ in range(N)]
  used = [False for _ in range(N)]
  input_graph(N)
  print(prim(N))

if __name__ == "__main__":
  main()
