import sys
import math
from collections import deque
import heapq
import itertools
MAX_INT = int(10e10)
MIN_INT = -MAX_INT
mod = 1000000007
sys.setrecursionlimit(1000000)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

X = I()

a = [0,1]
for i in range(2,300):
  a.append(i**5)
#print(a)

for i,j in itertools.combinations(a, 2):
  #print(i,j)
  for k in [-1,1]:
    if j - i*k == X:
      print(int(j**0.2), int(i**0.2)*k)
      exit()
print(error)