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

H, W, K = list(map(int, input().split()))
A = [list(input()) for _ in range(H)]

b = "#"
r = "."

for i in range(H):
  for j in range(W):
    if A[i][j] == b:
      A[i][j] = -1
    elif A[i][j] == r:
      A[i][j] = 0
    else:
      A[i][j] = 0
      S = [i, j]

if S[0] == 0 or S[0] == H - 1:
  print(0)
  exit()
if S[1] == 0 or S[1] == W - 1:
  print(0)
  exit()
g = gridMan(A)
g.makeWall()

L, r = g.dist(S)

ans = 10 ** 10
for i in range(H):
  for j in range(W):
    if 0 <= L[i][j] and L[i][j] <= K:
      t = min(i, j, H - i - 1, W - j - 1)
      if t == 0:
        print(1)
        exit()
      t = (t + K - 1) // K
      ans = min(ans, t)

print(ans + 1)