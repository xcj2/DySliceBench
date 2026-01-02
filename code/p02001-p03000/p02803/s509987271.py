import queue
h, w = map(int, input().split())
m = []
for i in range(h):
  m.append(input())
#print(h, w)
#print(m)
q = queue.Queue()
a = []
def init():
  global a
  a = []
  for i in range(h):
    a.append([-1] * w)

def bfs(cx, cy):
  nxs = [1, 0, -1, 0]
  nys = [0, -1, 0, 1]
  for i in range(4):
    nx = cx + nxs[i]
    ny = cy + nys[i]
    if 0 <= nx and nx < w and 0 <= ny and ny < h and m[ny][nx] == '.' and a[ny][nx] == -1:
      a[ny][nx] = a[cy][cx] + 1
      q.put([nx, ny])
  
def check(start_x, start_y):
  if m[start_y][start_x] == '#':
    return 0
  
  global a, q
  init()
  q.put([start_x, start_y])
  a[start_y][start_x] = 0
  end_x = -1
  end_y = -1
  while not q.empty():
    cx, cy = q.get()
    bfs(cx, cy)
    end_x = cx
    end_y = cy
  return a[end_y][end_x]

ans = 0
for i in range(h * w - 1):
    start_x = i % w
    start_y = i // w
    ans = max(ans, check(start_x, start_y))
    
print(ans)