import sys
import math
MAX_INT = int(10e15)
MIN_INT = -MAX_INT
mod = 1000000007
sys.setrecursionlimit(1000000)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

N = I()
data = [[] for i in range(N+1)]

for i in range(N):
  a = I()
  for j in range(a):
    data[i].append(IL())

ans = 0
for i in range(1 << N):
  TF = [-1]*N
  cnt = 0
  for j in range(N):
    if ((i >> j) & 1) == 1: #j人目が正しい
      TF[j] = True
      cnt += 1
    else:
      TF[j] = False
  
  for k in range(N):
    if TF[k] == True:
      for x,y in data[k]:
        if TF[x-1] == y:
          continue
        else:
          break
      else:
        continue
      break
  else:
    ans = max(ans, cnt)

print(ans)