while True:
  px, py = map(int, input().split())
  if px == 0:
    break

  n = int(input())
  pairs = list(map(int, input().split()))
  s_points = []
  for i in range(n):
    s_points.append((pairs[i * 2], pairs[i * 2 + 1]))
  
  survive_range = [(x, y) for x in (-1, 0, 1) for y in (-1, 0, 1)]
  jump_to = ((-2, -1), (-2, 0), (-2, 1), (-1, -2), (-1, 2), (0, -2), (0, 2), 
               (1, -2), (1, 2), (2, -1), (2, 0), (2, 1))

  def next_points(p):
    x, y = p
    return {(x + dx, y + dy) for dx, dy in jump_to if 0 <= x + dx <= 9 and 0 <= y + dy <= 9}

  def survive_points(p):
    x, y = p
    return {(x + dx, y + dy) for dx, dy in survive_range if 0 <= x + dx <= 9 and 0 <= y + dy <= 9}
  
  def next_survive(ps):
    ret = set()
    for p in ps:
      ret = ret | next_points(p)
    return ret

  survive ={(px, py)}
  for sp in s_points:
    i_survive = survive_points(sp)
    survive = next_survive(survive) & i_survive
  
  if survive:
    print("OK")
  else:
    print("NA")
