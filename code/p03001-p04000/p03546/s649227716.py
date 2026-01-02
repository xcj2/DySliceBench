from functools import reduce
from operator import add
from collections import Counter

H, W = list(map(int, input().split()))
C = [list(map(int, input().split())) for _ in range(10)]
A = [list(map(int, input().split())) for _ in range(H)]
A = reduce(add, A)
c = Counter(A)

class WarshallFloyd():
  def __init__(self, matrix):
    self.inf = 1e12
    self.v = len(matrix)
    self.e = matrix
    self.K = [[self.inf]*self.v for _ in range(self.v)]
    self.newK = self.K.copy()
    self.calculated = False
    
  def calc(self):
    for k in range(self.v):
      for i in range(self.v):
        self.newK[i][k] = min([self.K[i][k], self.e[i][k]])
        self.newK[k][i] = min([self.K[k][i], self.e[k][i]])

      for i in range(self.v):
        for j in range(self.v):
          if i!=j and i!=k and j!=k:
            self.newK[i][j] = min([self.K[i][j], self.newK[i][k]+self.newK[k][j]])
      self.K = self.newK.copy()
    self.calculated = True
    return self.K
  
  def shortest_way(self,a,b):
    if not self.calculated:
      self.calc()
    return self.K[a][b]

wf = WarshallFloyd(C)
wf.calc()

answer = 0
for k,v in c.items():
  if k!=-1:
    answer += v * wf.shortest_way(k,1)
print(answer)