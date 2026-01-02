board = [int(s) for _ in range(4) for s in input().split()]
move_piece = [None]* 46
GOAL = list(range(1,16)) + [0]


def create_adjacent(h, w):
  adjacent = [[] for _ in range(h*w)]
  for i in range(h * w):
    if i % w != w-1:
      adjacent[i].append(i+1)
    if i % w != 0:
      adjacent[i].append(i-1)
    if i // h < h-1:
      adjacent[i].append(i+w)
    if i // h > 0:
      adjacent[i].append(i-w)
  return adjacent

def id_search(limit, move, space, lower):
  if move == limit:
    if board == GOAL:
      global count
      count += 1
      print(move)
      exit()
  else:
    for x in adjacent[space]:
      p = board[x]
      if move_piece[move] == p:
        continue
      board[space], board[x] = p, 0
      move_piece[move + 1] = p
      new_lower = lower - distance[p][x] + distance[p][space]

      if new_lower + move <= limit:
        id_search(limit, move+1, x, new_lower)
      board[space], board[x] = 0, p

def create_distance(h, w):
  distance = [[0] * h * w for _ in range(h *w)]
  for i in range(h*w):
    if i == 0:
      continue
    ye, xe = divmod(i-1, w)
    for j in range(h *w):
      y, x = divmod(j,w)
      distance[i][j] = abs(ye-y) + abs(xe-x)
  return distance

def get_distance(board):
  v = 0
  for x in range(len(board)):
    p = board[x]
    if p == 0:
      continue
    v += distance[p][x]
  return v

adjacent = create_adjacent(4, 4)
distance = create_distance(4,4)
n = get_distance(board)
count = 0
for x in range(n,46):
  id_search(x, 0, board.index(0), n)
  if count > 0:
    break


