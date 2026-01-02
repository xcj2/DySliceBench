import sys

# D - Wizard in Maze
def get_index(s):
	return int(s) - 1


def search_nearby(h, w):
# 上下左右に隣接するマスを探索
	search(h + 1, w, False)
	search(h - 1, w, False)
	search(h, w + 1, False)
	search(h, w - 1, False)


def search_using_warp(h, w):
  # ワープ魔法で移動できるマスを探索
  for i in range(-2, 3):
    search(h - 2, w + i)
    search(h + 2, w + i)

  for i in range(-2, 3):
    if i != 0:
      search(h - 1, w + i)
      search(h + 1, w + i)

  search(h, w + 2)
  search(h, w - 2)


def search(h, w, is_using_warp = True):
  global is_reached
  global que
  global next_que

  if can_reach(h, w):
	  is_reached[h][w] = True
	  next_que.append([h, w])

	  if not is_using_warp:
	    que.append([h, w])


def can_reach(h, w):
	global H
	global W
	global maze

	if h < 0 or h >= H or w < 0 or w >= W:
		return False
	elif maze[h][w] == '#':
		return False
	elif is_reached[h][w]:
		return False
	else:
		return True


from collections import deque
import copy

H, W = map(int, input().split())
Ch, Cw = map(get_index, input().split())
Dh, Dw = map(get_index, input().split())

maze = []

for _ in range(H):
	maze.append(input())

is_reached = [[False] * W for _ in range(H)]

next_que = deque()
next_que.append([Ch, Cw])
mp = 0

while len(next_que) > 0:
  que = copy.deepcopy(next_que)

	# コストiで到達可能なマスを列挙
  while len(que) > 0:
    h, w = que.popleft()
    is_reached[h][w] = True

    search_nearby(h, w)

  if is_reached[Dh][Dw]:
    print(mp)
    exit()

  que = copy.deepcopy(next_que)
  next_que.clear()
  mp += 1

	# コストiで到達可能なマスを列挙
  while len(que) > 0:
    h, w = que.popleft()
    is_reached[h][w] = True

    search_using_warp(h, w)

  if is_reached[Dh][Dw]:
    print(mp)
    exit()

print(-1)