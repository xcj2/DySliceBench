import queue
class gridMan:
  def __init__(s, L):
    s.L = L
    s.H = len(s.L)
    s.W = len(s.L[0])
  def makeWall(s, x = -2):
    w = len(s.L[0]) + 2
    s.L = [[x] * w] + [[x] + i + [x] for i in s.L] + [[x] * w]
  def dist(s, S): #Sから上下左右に進んで何手かかるかのリスト　および　最大値
    T = [[-1] * s.W for _ in range(s.H)]
    q = queue.Queue()
    q.put([S[0], S[1]])
    T[S[0]][S[1]] = 0
    k = 0
    while not q.empty():
      h, w = q.get()
      k = T[h][w]
      for i, j in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        hh = h + i
        ww = w + j
        if s.L[hh + 1][ww + 1] >= 0 and T[hh][ww] == -1:
          q.put([hh, ww])
          T[hh][ww] = k + 1
    return T, k

H, W = list(map(int, input().split()))
s = [list(input()) for _ in range(H)]

ans = 0
D = [[0] * W for _ in range(H)]
for i in range(H):
  for j in range(W):
    if s[i][j] == ".":
      D[i][j] = 0
      ans += 1
    else:
      D[i][j] = -1

g = gridMan(D)
g.makeWall()

L, ma = g.dist([0, 0])

if L[-1][-1] == -1:
  print(-1)
  exit()

print(ans - L[-1][-1] - 1)


