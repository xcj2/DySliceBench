import math
import functools
import itertools
import numpy as np
import sys
MAX_INT = int(10e10)
MIN_INT = -MAX_INT
mod = 1000000007
sys.setrecursionlimit(1000000)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

N,K = IL()
s = S()

left_List = [0]
left = 0
flag = ""
cnt = 0
j = 0
ans = 0
for i in range(N):
  if i != 0:
    if flag == 0:
      if s[i] == "1":
        left_List.append(i)
        cnt += 1
    else:
      if cnt >= K:
        if s[i] == "0":
          ans = max(ans, i-left_List[j])
          j += 1

  if s[i] == "0":
    flag = 0
  else:
    flag = 1

else:
  ans = max(ans, N-left_List[j])

print(ans)