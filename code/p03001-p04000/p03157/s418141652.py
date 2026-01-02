from collections import deque

H, W = map(int, input().split())
S = [input() for _ in range(H)]

check = [[1 for _ in range(W)] for _ in range(H)]

def bw(s):
  if s == "#":
    return "."
  else:
    return "#"

def cnt_plus(s, cnt):
  if s == "#":
    c = [cnt[0] + 1, cnt[1]]
  else:
    c = [cnt[0], cnt[1] + 1]
  return c
  
def bfs(i, j):
  stack = deque()
  stack.append(((i, j), S[i][j]))
  check[i][j] = 0
  cnt = [0, 0]
  
  while stack:
    p, s = stack.popleft()
    cnt = cnt_plus(s, cnt)
    ii, jj = p
    bws = bw(s)

    if ii - 1 >= 0 and check[ii - 1][jj]:
      if S[ii - 1][jj] == bws:
        check[ii - 1][jj] = 0
        stack.append(((ii - 1, jj), bws))

    if ii + 1 < H and check[ii + 1][jj]:
      if S[ii + 1][jj] == bws:
        check[ii + 1][jj] = 0
        stack.append(((ii + 1, jj), bws))

    if jj - 1 >= 0 and check[ii][jj - 1]:
      if S[ii][jj - 1] == bws:
        check[ii][jj - 1] = 0
        stack.append(((ii, jj - 1), bws))

    if jj + 1 < W and check[ii][jj + 1]:
      if S[ii][jj + 1] == bws:
        check[ii][jj + 1] = 0
        stack.append(((ii, jj + 1), bws))
  return cnt[0] * cnt[1]

answer = 0
for i in range(H):
  for j in range(W):
    if check[i][j] and S[i][j] == "#":
      answer += bfs(i, j)
print(answer)