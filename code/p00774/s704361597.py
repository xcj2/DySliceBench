class Puzzle():
  def __init__(self, mat, N):
    self.mat = mat
    self.h = N
    self.score = 0

  def calc(self):
    tmp_score = self.score

    for i in range(self.h):
      for j in range(3):
        if self.mat[i][j] > 0:
          # 5,2
          for k in range(5, 2, -1):
            if j+k <= 7 and k-j >= 3:
              s = set(self.mat[i][j:k])
              if len(s) == 1 and -1 not in s:
                tmp_score += list(s)[0] * (k-j)
                for l in range(j, k):
                  self.mat[i][l] = -1
                break

    if self.score >= tmp_score:
      return False
    else:
      self.score = tmp_score
      return True

  def flatten(self):
    pivot_mat = []
    for i in range(5):
      row = []
      for j in range(self.h):
        if self.mat[j][i] != -1:
          row.append(self.mat[j][i])

      short = self.h - len(row)
      if short > 0:
        row.reverse()
        for k in range(short):
          row.append(-1)
        row.reverse()
      
      pivot_mat.append(row)

    mat = [ [-1]*5 for i in range(self.h) ]
    for i in range(self.h):
      for j in range(5):
        mat[i][j] = pivot_mat[j][i]

    self.mat = mat

while True:
  h = int(input())
  if h==0: exit()
  mat = []
  for _ in range(h):
    mat.append(list(map(int,input().split())))
  puzzle = Puzzle(mat, h)

  while True:
    if puzzle.calc():
      puzzle.flatten()
    else:
      break

  print(puzzle.score)
