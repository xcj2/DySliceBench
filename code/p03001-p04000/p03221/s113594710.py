def get_line():
  return input().split(' ')

class element:
  def __init__(self, P, Y, idx):
    self.P = P
    self.Y = Y
    self.idx = idx
  def __lt__(self, other):
    return self.Y < other.Y

N, M = map(int, get_line())
els = [0] * M
for i in range(M):
  p, y = map(int, get_line())
  els[i] = element(p, y, i)

p_map = [[] for _ in range(N)]

for e in els:
  p_map[e.P - 1].append(e)

ans = [0] * M

for mp in p_map:
  cnt = 1
  for e in sorted(mp):
    ans[e.idx] = "{:06d}{:06d}".format(e.P, cnt)
    cnt = cnt + 1

for e in ans:
  print(e)
