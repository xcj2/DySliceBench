import heapq
from heapq import heapify, heappush, heappop

global G

def input_graph(M, uvab):
  global G
  for i in range(M):
    u, v, a, b = uvab[i]
    G[u-1] += [[v-1, (a, b)]]
    G[v-1] += [[u-1, (a, b)]]
  
def dijkstra(N, S, flag):
  global G
  dist = [float('inf') for _ in range(N)]
  dist[S] = 0
  Q = [(0, S)]
  while Q:
    c, v = heappop(Q)
    if dist[v] < c:
      continue
    for t, cost in G[v]:
      yen, snuuk = cost
      if flag:
        if dist[v] + yen < dist[t]:
          dist[t] = dist[v] + yen
          heappush(Q, (dist[t], t))
      else:
        if dist[v] + snuuk < dist[t]:
          dist[t] = dist[v] + snuuk
          heappush(Q, (dist[t], t))
  return dist

def main():
  global G
  N, M, S, T = map(int, input().split())
  S -= 1
  T -= 1
  uvab = [list(map(int, input().split())) for _ in range(M)]
  G = [[] for _ in range(N)]
  input_graph(M, uvab)
  yen_dist = dijkstra(N, S, True)
  snuuk_dist = dijkstra(N, T, False)
  dist = [yen_dist[i]+snuuk_dist[i] for i in range(N)]
  for i in range(N-2, -1, -1):
    dist[i] = min(dist[i+1], dist[i])
  for i in range(N):
    print(10**15-dist[i])

if __name__ == "__main__":
  main()