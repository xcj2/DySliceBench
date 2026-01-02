from sys import exit, setrecursionlimit, stderr
from functools import reduce
from itertools import *
from collections import *
from bisect import *

def read():
  return int(input())
 
def reads():
  return [int(x) for x in input().split()]

N = read()
A = []
for _ in range(N):
  A.append(reads())

necc = [[True] * N for _ in range(N)]

def fail():
  print(-1); exit()

for i, j, k in combinations(range(N), 3):
  if A[i][j] + A[j][k] < A[i][k] or A[i][j] + A[i][k] < A[j][k] or A[i][k] + A[j][k] < A[i][j]:
    fail()
  if A[i][j] + A[j][k] == A[i][k]:
    necc[i][k] = False
  if A[i][j] + A[i][k] == A[j][k]:
    necc[j][k] = False
  if A[i][k] + A[j][k] == A[i][j]:
    necc[i][j] = False

ans = sum(A[i][j] for i, j in combinations(range(N), 2) if necc[i][j])
print(ans)