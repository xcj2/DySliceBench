import sys
import bisect
MAX_INT = int(10e12)
MIN_NUM = -MAX_INT
mod = 1000000007
sys.setrecursionlimit(1000000000)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

def distance(list, index, x):
  res = abs(x - list[index][0])
  return res

def distance2(list, index, x):
  res = abs(x - list[index])
  return res

# 二分探索 #
def nibutan(list,n):
    left = -1
    right = len(list)
    while left+1 != right:
        middle = (left+right)//2
        if list[middle][0] <= n:
            left = middle
        else:
            right = middle
    return right

A,B,Q = IL()
a = [I() for i in range(A)] # 0
b = [I() for i in range(B)] # 1
q = [I() for i in range(Q)]
ab = []

a.sort()
b.sort()

for i in a:
  ab.append([i,0])
for i in b:
  ab.append([i,1])
ab.sort()

for x in q:
  ans = MAX_INT
  ID = nibutan(ab, x)
  for i in [-1,0]:
    if 0 <= ID+i < len(ab):
      if ab[ID+i][1] == 0: # a → b
        for j in [-1,0]:
          ID2 = bisect.bisect_left(b, ab[ID+i][0])
          if 0 <= ID2+j < len(b):
            dis = distance(ab, ID+i, x)
            dis += distance2(b, ID2+j, ab[ID+i][0])
            ans = min(ans, dis)
      else: # b → a
        for j in [-1,0]:
          ID2 = bisect.bisect_left(a, ab[ID+i][0])
          if 0 <= ID2+j < len(a):
            dis = distance(ab, ID+i, x)
            dis += distance2(a, ID2+j, ab[ID+i][0])
            ans = min(ans, dis)
  print(ans)