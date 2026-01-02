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
K = I()
N = len(s)

start = s[0]
left = 0
right = 0
f = 0
for i in range(N):
  if f == 0:
    if s[i] == start:
      left = i
    else:
      f = 1
if f == 0:
  ans = N*K//2
  print(ans)
else:
  if s[0] == s[-1]:
    f = 0
    for i in range(N-1,-1,-1):
      if f == 0:
        if s[i] == start:
          right = i
        else:
          f = 1
    left = left +1

    #print(left)
    #print(right)
    #print(((left + (N-right))//2)*(K-1))
    ans = ((left + (N-right))//2)*(K-1) + left//2  + (N-right)//2
  else:
    ans = 0
    left = 0
    right = N
  tmp = 0
  t = ""
  for i in range(left,right):
    if t == s[i]:
      tmp += 1
    else:
      t = s[i]
      tmp = 1
    if tmp%2 == 0:
      ans += K
  print(ans)