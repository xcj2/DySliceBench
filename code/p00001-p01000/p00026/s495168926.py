def small_ink(paper,x,y):
  paper[x][y] += 1
  if 0 <= x-1 and x-1 < 10:
    paper[x-1][y] += 1
  if 0 <= y-1 and y-1 < 10:
    paper[x][y-1] += 1
  if 0 <= x+1 and x+1 < 10:
    paper[x+1][y] += 1
  if 0 <= y+1 and y+1 < 10:
    paper[x][y+1] += 1
  return paper

def middle_ink(paper,x,y):
  paper = small_ink(paper,x,y)
  if (0 <= x-1 and x-1 < 10) and (0 <= y-1 and y-1 < 10):
    paper[x-1][y-1] += 1
  if (0 <= x-1 and x-1 < 10) and (0 <= y+1 and y+1 < 10):
    paper[x-1][y+1] += 1
  if (0 <= x+1 and x+1 < 10) and (0 <= y-1 and y-1 < 10):
    paper[x+1][y-1] += 1
  if (0 <= x+1 and x+1 < 10) and (0 <= y+1 and y+1 < 10):
    paper[x+1][y+1] += 1
  return paper

def large_ink(paper,x,y):
  paper = middle_ink(paper,x,y)
  if (0 <= x-2 and x-2 < 10):
    paper[x-2][y] += 1
  if (0 <= y-2 and y-2 < 10):
    paper[x][y-2] += 1
  if (0 <= y+2 and y+2 < 10):
    paper[x][y+2] += 1
  if (0 <= x+2 and x+2 < 10):
    paper[x+2][y] += 1
  return paper

paper = [([0 for _ in range(10)]) for _ in range(10)]

while True:
  try:
    x,y,s = map(int, input().split(','))
  except EOFError:
    break
  if s == 1:
    paper = small_ink(paper,x,y)
  elif s == 2:
    paper = middle_ink(paper,x,y)
  elif s == 3:
    paper = large_ink(paper,x,y)

sum0 = 0
max_ink = 0
for i in range(10):
  for j in range(10):
    if paper[i][j] == 0:
      sum0 += 1
    if paper[i][j] > max_ink:
      max_ink = paper[i][j]
print(sum0)
print(max_ink)
