import sys
sys.setrecursionlimit(1000000)
INF = 10 ** 20

def update_state(state, newx):
  tmp = list(state)
  tmp[newx] = 1
  return tuple(tmp)

def get_co(x, y):
  dc = do = 0
  score = mp[y][x]
  if score < 0:
    dc = -score
  else:
    do = score
  return dc, do

def minimum_cost(x, y, state, ox, goal, dic, w, m):
  if (x, y, state, ox) in dic:
    return dic[(x, y, state, ox)]
  if y == goal:
    return 0
  if ox <= 1:
    return INF
  
  ret = INF
  
  if x >= 1:
    if state[x - 1] == 0:
      dc, do = get_co(x - 1, y)
      ret = min(ret, minimum_cost(x - 1, y, update_state(state, x - 1), min(ox + do - 1, m), goal, dic, w, m) + dc)
    else:
      ret = min(ret, minimum_cost(x - 1, y, state, ox - 1, goal, dic, w, m))
  
  if x < w - 1:
    if state[x + 1] == 0:
      dc, do = get_co(x + 1, y)
      ret = min(ret, minimum_cost(x + 1, y, update_state(state, x + 1), min(ox + do - 1, m), goal, dic, w, m) + dc)
    else:
      ret = min(ret, minimum_cost(x + 1, y, state, ox - 1, goal, dic, w, m))
 
 
  dc, do = get_co(x, y + 1)
  ret = min(ret, minimum_cost(x, y + 1, tuple((1 if i == x else 0 for i in range(w))), min(ox + do - 1, m), goal, dic, w, m) + dc)
  dic[(x, y, state, ox)] = ret
  return ret

while True:
  w, h = map(int, input().split())
  if w == 0:
    break
  f, m, o = map(int, input().split())
  mp = [list(map(int, input().split())) for _ in range(h)]
  if o <= 1:
    print("NA")
    continue
  dic = {}
  ans = INF
  for i in range(w):
    dc, do = get_co(i, 0)
    state = tuple(1 if i == j else 0 for j in range(w))
    ans = min(ans, minimum_cost(i, 0, state, min(o + do - 1, m), h - 1, dic, w, m) + dc)
  if ans > f:
    print("NA")
  else:
    print(ans)
