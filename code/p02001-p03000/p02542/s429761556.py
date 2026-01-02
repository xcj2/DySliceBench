import heapq
NUMERIC_LIMITS = 10 ** 18

class mcf_graph:
  def __init__ (s, n):
    s._n = n
    s.g = [[] for _ in range(n)]
    s.pos = []

  def add_edge(s, frm, to, cap, cost):
    m = len(s.pos)
    s.pos.append([frm, len(s.g[frm])])
    s.g[frm].append(s._edge(to, len(s.g[to]), cap, cost))
    s.g[to].append(s._edge(frm, len(s.g[frm]) - 1, 0, -cost))
    return m

  class edge:
    __slots__ = "frm", "to", "cap", "flow", "cost"
    def __init__(s, frm, to, cap, flow, cost):
      s.frm, s.to = frm, to
      s.cap, s.flow, s.cost = cap, flow, cost

  def get_edge(s, i):
    _e = s.g[s.pos[i][0]][s.pos[i][1]]
    _re = s.g[_e.to][_e.rev]
    return s.edge(s.pos[i][0], _e.to, _e.cap + _re.cap, _re.cap, _e.cost)

  def edges(s):
    for i in range(len(s.pos)):
      yield s.get_edge(i)

  def flow(self, s, t, flow_limit = NUMERIC_LIMITS):
    return self.slope(s, t, flow_limit)[-1]

  def dual_ref(self, s, t):
    #priority_queueの代わり
    push = heapq.heappush
    pop = heapq.heappop

    dist = [NUMERIC_LIMITS] * self._n
    self.pv = [-1] * self._n
    self.pe = [-1] * self._n
    vis = [False] * self._n
    que = []
    dist[s] = 0
    push(que, (0, s))
    while que:
      k, v = pop(que)
      if vis[v]: continue
      vis[v] = True
      if v == t: break
      for i in range(len(self.g[v])):
        e = self.g[v][i]
        if vis[e.to] or not e.cap: continue
        cost = e.cost - self.dual[e.to] + self.dual[v]
        if dist[e.to] - dist[v] > cost:
          dist[e.to] = dist[v] + cost
          self.pv[e.to] = v
          self.pe[e.to] = i
          push(que,(dist[e.to], e.to))
    if not vis[t]: return False
    for v in range(self._n):
      if not vis[v]: continue
      self.dual[v] -= dist[t] - dist[v]
    return True

  def slope(self, s, t, flow_limit = NUMERIC_LIMITS):
    self.dual = [0] * self._n
  
    flow = 0
    cost, prev_cost = 0, -1
    result = [(flow,cost)]
    while flow < flow_limit:
      if not self.dual_ref(s, t): break
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
    def __init__(s, to, rev, cap, cost):
      s.to, s.rev = to, rev
      s.cap, s.cost = cap, cost


N, M = list(map(int, input().split()))
s = [list(input()) for _ in range(N)]

flow = mcf_graph(N * M + 2)
S = N * M
T = N * M + 1
ans = 0
cnt = 0
for n in range(N):
  for m in range(M):
    if s[n][m] == "#": continue
    x = n * M + m
    if m + 1 < M:
      if s[n][m + 1] != "#":
        y = n * M + m + 1
        flow.add_edge(x, y, N * M, 0)
    if n + 1 < N:
      if s[n + 1][m] != "#":
        y = (n + 1) * M + m
        flow.add_edge(x, y, N * M, 0)
    if s[n][m] == "o":
      flow.add_edge(S, x, 1, 0)
      ans += n + m
      cnt += 1
    flow.add_edge(x, T, 1, N + M -(n + m))

f = flow.flow(S, T, cnt)[1]

print((N + M) * cnt - f - ans)

