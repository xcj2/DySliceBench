import itertools
import sys

def f_row(L):
  for i in range(3):
    for j in range(3):
      if L[i][j] == False:
        break
      elif j == 2:
        return True
      else:
        continue
  return False

def f_col(L):
  for i in range(3):
    for j in range(3):
      if L[j][i] == False:
        break
      elif j == 2:
        return True
      else:
        continue
  return False
        
def f_rcross(L):
  for i in range(3):
    if L[i][i] == False:
      break
    elif i == 2:
      return True
    else:
      continue
  return False
      
def f_lcross(L):
  for i in range(3):
    if L[i][2-i] == False:
      break
    elif i == 2:
      return True
    else:
      continue
  return False

A = [list(map(int, input().split())) for _ in range(3)]
N = int(input())
B = [int(input()) for _ in range(N)]

L = [[0]*3 for _ in range(3)]

for b in B:
  for i, j in itertools.product(range(3), repeat=2):
    if b == A[i][j]:
      L[i][j] = True
      if f_row(L) or f_col(L) or f_rcross(L) or f_lcross(L):
        print('Yes')
        sys.exit()
      break
print('No')