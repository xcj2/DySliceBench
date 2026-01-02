import sys
import math
from collections import deque
import heapq
import itertools
import bisect
MAX_INT = int(10e10)
MIN_INT = -MAX_INT
mod = 1000000007
sys.setrecursionlimit(1000000)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

N = I()
a = IL()

for i in range(N):
  a[i] -= i
#print(a)

b = a[:]
b.sort()

#print(b)
ans = 0
for i in range(N):
  num = -((i+1) - 1)*2 - a[i]
  #print(i+1, num)
  #print(bisect.bisect_right(b, num))
  #print(bisect.bisect_left(b, num))
  #print("---")
  ans += bisect.bisect_right(b, num) - bisect.bisect_left(b, num)
print(ans)