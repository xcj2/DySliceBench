import math
import sys
MAX_INT = int(10e15)
MIN_INT = -MAX_INT
mod = 1000000007
sys.setrecursionlimit(1000000)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

a = []
for i in range(3):
  n = IL()
  for j in n:
    a.append(j)

N = I()
used = [False]*9
for _ in range(N):
  n = I()
  for i in range(9):
    if a[i] == n:
      used[i] = True

f = 0
if all(used[0:3]) or all(used[3:6]) or all(used[6:9]):
  f = 1
if (used[0] and used[3] and used[6]) or (used[1] and used[4] and used[7]) or (used[2] and used[5] and used[8]):
  f = 1
if (used[0] and used[4] and used[8]):
  f = 1
if (used[2] and used[4] and used[6]):
  f = 1
if f == 0:
  print("No")
else:
  print("Yes")