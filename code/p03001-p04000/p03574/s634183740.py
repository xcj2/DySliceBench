h, w = map(int, input().split())

s = []
for si in range(h):
  s.append(list(input()))

def up_left(s, x, y):
  if x - 1 < 0 or y - 1 < 0:
    return 0
  return 1 if s[y - 1][x - 1] == '#' else 0

def up(s, x, y):
  if y - 1 < 0:
    return 0
  return 1 if s[y - 1][x] == '#' else 0

def up_right(s, x, y, w):
  if y - 1 < 0 or x + 1 >= w:
    return 0
  return 1 if s[y - 1][x + 1] == '#' else 0

def left(s, x, y):
  if x - 1 < 0:
    return 0
  if s[y][x-1] == '#':
    return 1
  return 0

def right(s, x, y, w):
  if x + 1 >= w:
    return 0
  return 1 if s[y][x + 1] == '#' else 0

def down_left(s, x, y, h):
  if y + 1 >= h or x - 1 < 0:
    return 0
  return 1 if s[y + 1][x - 1] == '#' else 0

def down(s, x, y, h):
  if y + 1 >= h:
    return 0
  return 1 if s[y + 1][x] == '#' else 0

def down_right(s, x, y, h, w):
  if y + 1 >= h or x + 1 >= w:
    return 0
  return 1 if s[y + 1][x + 1] == '#' else 0
  
rr = []
for y_i, sy in enumerate(s):
  r = []
  for x_i, x in enumerate(sy):
    bomb_count = 0
    if x == '#':
      r.append(x)
    else:
      # 1
      bomb_count += up_left(s, x_i, y_i)
      bomb_count += up(s, x_i, y_i)
      bomb_count += up_right(s, x_i, y_i, w)
      bomb_count += left(s, x_i, y_i)
      bomb_count += right(s, x_i, y_i, w)
      bomb_count += down_left(s, x_i, y_i, h)
      bomb_count += down(s, x_i, y_i, h)
      bomb_count += down_right(s, x_i, y_i, h, w)
      r.append(str(bomb_count))
  rr.append(r)
    
for ri in rr:
  print(''.join(ri))
  