from heapq import heappop, heappush

NUMERIC_LIMITS = (1 << 63) - 1
INF = 10 ** 9

class McfGraph:
  def __init__(self, n):
    self._n = n
    self.g = [[] for _ in range(n)]
    self.pos = []
 
  def add_edge(self, frm, to, cap, cost):
    m = len(self.pos)
    self.pos.append([frm, len(self.g[frm])])
    self.g[frm].append(self._edge(to, len(self.g[to]), cap, cost))
    self.g[to].append(self._edge(frm, len(self.g[frm]) - 1, 0, -cost))
    return m
 
  class edge:
    __slots__ = "frm", "to", "cap", "flow", "cost"
 
    def __init__(self, frm, to, cap, flow, cost):
      self.frm, self.to = frm, to
      self.cap, self.flow, self.cost = cap, flow, cost
 
  def get_edge(self, i):
    _e = self.g[self.pos[i][0]][self.pos[i][1]]
    _re = self.g[_e.to][_e.rev]
    return self.edge(self.pos[i][0], _e.to, _e.cap + _re.cap, _re.cap, _e.cost)
 
  def edges(self):
    for i in range(len(self.pos)):
      yield self.get_edge(i)
 
  def flow(self, s, t, flow_limit=NUMERIC_LIMITS):
    return self.slope(s, t, flow_limit)[-1]
 
  def dual_ref(self, s, t):
    dist = [NUMERIC_LIMITS] * self._n
    self.pv = [-1] * self._n
    self.pe = [-1] * self._n
    vis = [False] * self._n
    que = []
    dist[s] = 0
    heappush(que, (0, s))
    while que:
      _, v = heappop(que)
      if vis[v]:
        continue
      vis[v] = True
      if v == t:
        break
      for i in range(len(self.g[v])):
        e = self.g[v][i]
        if vis[e.to] or not e.cap:
          continue
        cost = e.cost - self.dual[e.to] + self.dual[v]
        if dist[e.to] - dist[v] > cost:
          dist[e.to] = dist[v] + cost
          self.pv[e.to] = v
          self.pe[e.to] = i
          heappush(que, (dist[e.to], e.to))
    if not vis[t]:
      return False
    for v in range(self._n):
      if not vis[v]:
        continue
      self.dual[v] -= dist[t] - dist[v]
    return True
 
  def slope(self, s, t, flow_limit=NUMERIC_LIMITS):
    self.dual = [0] * self._n
 
    flow = 0
    cost, prev_cost = 0, -1
    result = [(flow, cost)]
    while flow < flow_limit:
      if not self.dual_ref(s, t):
        break
      c = flow_limit - flow
      v = t
      while v != s:
        c = min(c, self.g[self.pv[v]][self.pe[v]].cap)
        v = self.pv[v]
      v = t
      while v != s:
        e = self.g[self.pv[v]][self.pe[v]]
        e.cap -= c
        self.g[v][e.rev].cap += c
        v = self.pv[v]
      d = -self.dual[s]
      flow += c
      cost += c * d
      if prev_cost == d:
        result.pop()
      result.append((flow, cost))
      prev_cost = cost
    return result
 
  class _edge:
    __slots__ = "to", "rev", "cap", "cost"
 
    def __init__(self, to, rev, cap, cost):
      self.to, self.rev, self.cap, self.cost = to, rev, cap, cost
 
 
def atcoder_practice2_e():
    import sys
    input = sys.stdin.buffer.readline
 
    N, K = list(map(int, input().split()))
    A = [tuple(map(int, input().split())) for _ in range(N)]
    BIG = 10 ** 9
 
    g = McfGraph(2 * N + 2)
    s = 2 * N
    t = 2 * N + 1
 
    g.add_edge(s, t, N * K, BIG)
 
    for i in range(N):
        g.add_edge(s, i, K, 0)
        g.add_edge(N + i, t, K, 0)
    for i in range(N):
        for j in range(N):
            g.add_edge(i, N + j, 1, BIG - A[i][j])
 
    result = g.flow(s, t, N * K)
    print(N * K * BIG - result[1])
 
    grid = [["."] * N for _ in range(N)]
    edges = g.edges()
    for e in edges:
        if e.frm == s or e.to == t or e.flow == 0:
            continue
        grid[e.frm][e.to - N] = "X"
 
    for g in grid:
        print("".join(g))


N, M = map(int, input().split())
board = [input().strip() for i in range(N)]

g = McfGraph(M * N + 2)
s = M * N
t = M * N + 1

need = 0

for i in range(N):
    for j in range(M):
        if board[i][j] == 'o':
            need += 1
            g.add_edge(s, M * i + j, 1, i + j)

        if board[i][j] != '#':
            g.add_edge(M * i + j, t, 1, N + M - 2 - i - j)

            if i + 1 < N and board[i + 1][j] != '#':
                g.add_edge(M * i + j, M * (i + 1) + j, INF, 0)

            if j + 1 < M and board[i][j + 1] != '#':
                g.add_edge(M * i + j, M * i + j + 1, INF, 0)

flow, cost = g.flow(s, t, need)
opt = (N + M - 2) * need
print(opt - cost)
 
