#import numpy as np
import math
import sys
import itertools
MAX_INT = int(10e12)
MIN_INT = -MAX_INT
mod = 1000000007
sys.setrecursionlimit(1000000000)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

s = S()
x,y = IL()
N = len(s)

xlist = []
ylist = []

f = 0
cnt = 0
for i in range(N):
  if s[i] == "F":
    cnt += 1
  elif s[i] == "T":
    if f == 0:
      xlist.append(cnt)
      f = 1
    else:
      ylist.append(cnt)
      f = 0
    cnt = 0
else:
  if f == 0:
    xlist.append(cnt)
  else:
    ylist.append(cnt)

x -= xlist.pop(0)
Xsum = sum(xlist)
Ysum = sum(ylist)

if (Xsum-x)%2 != 0:
  print("No")
  exit()
else:
  Xnum = (Xsum-abs(x))//2
if (Ysum-y)%2 != 0:
  print("No")
  exit()
else:
  Ynum = (Ysum-abs(y))//2

#print(Xnum,Ynum)

XDP = [[0]*(abs(Xnum)+1) for _ in range(len(xlist)+1)]
YDP = [[0]*(abs(Ynum)+1) for _ in range(len(ylist)+1)]

XDP[0][0] = 1
YDP[0][0] = 1

for i in range(1,len(xlist)+1):
  for j in range(Xnum+1):
    if XDP[i-1][j] == 1:
      XDP[i][j] = 1
      if j+xlist[i-1] < Xnum+1:
        XDP[i][j+xlist[i-1]] = 1
#print(Xnum)
#print(xlist)
#print(XDP)

for i in range(1,len(ylist)+1):
  for j in range(Ynum+1):
    if YDP[i-1][j] == 1:
      YDP[i][j] = 1
      if j+ylist[i-1] < Ynum+1:
        YDP[i][j+ylist[i-1]] = 1
#print(Ynum)
#print(ylist)
#print(YDP)

if XDP[-1][-1] == 1 and YDP[-1][-1] == 1:
  print("Yes")
else:
  print("No")