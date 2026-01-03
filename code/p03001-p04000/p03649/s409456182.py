from sys import exit, setrecursionlimit, stderr
from functools import reduce
from itertools import *
from collections import *
from bisect import bisect
 
def read():
  return int(input())
 
def reads():
  return [int(x) for x in input().split()]

N = read()
A = [a-(N-1) for a in reads()]

def possible(x): # possible at exactly x-th turn
  return sum((a + x + N) // (N+1) for a in A if a + x > 0) <= x

l = -1; r = 10 ** 19
while r - l > 1:
  m = (l + r) // 2
  if possible(m):
    r = m
  else:
    l = m
ans = min(x for x in range(l - 10*N**2, l + 10*N**2) if possible(x))
print(ans)

