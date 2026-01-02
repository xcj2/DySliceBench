import numpy as np
import sys
input = sys.stdin.readline
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

def imos():
  for j in range(N+1):
    cnt = 0
    for i in range(N+1):
      tmp = l[j][i]
      l[j][i] += cnt
      cnt += tmp

  for j in range(N+1):
    cnt = 0
    for i in range(N+1):
      tmp = l[i][j]
      l[i][j] += cnt
      cnt += tmp

N,M,Q = IL()
l = [[0]*(N+1) for i in range(N+1)]
for i in range(M):
  a,b = IL()
  l[1][b] += 1
  if a+1 <= N:
    l[a+1][b] += -1

imos()

ans = [IL() for i in range(Q)]
for i in range(Q):
    print(l[ans[i][0]][ans[i][1]])