#### import ####
import sys
import math
from collections import defaultdict

#### 設定 ####
sys.setrecursionlimit(10**7)
def input():
  return sys.stdin.readline()[:-1]

#### 定数 ####
mod = 10**9 + 7

#### 読み込み ####
def I(): return int(input())
def II(): return map(int, input().split())
def III(): return list(map(int, input().split()))
def Line(N):
  read_all = [tuple(map(int, input().split())) for _ in range(N)]
  return map(list,zip(*read_all))

#################

N = I()
A = III()
B = III()

counter = 0
for i in range(N):
  if A[i]+A[i+1] <= B[i]:
    counter += A[i]+A[i+1]
    A[i+1]=0
  elif A[i] < B[i]:
    counter += B[i]
    A[i+1] -= B[i]-A[i]
  else:
    counter += B[i]
print(counter) 