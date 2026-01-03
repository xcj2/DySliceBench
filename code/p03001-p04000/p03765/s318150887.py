from sys import exit, setrecursionlimit, stderr
from functools import reduce
from itertools import *
from collections import *
from bisect import bisect
from heapq import *

def read():
  return int(input())
 
def reads():
  return [int(x) for x in input().split()]

def enc(s):
  return [(1 if c == 'A' else 2) for c in s]

S = enc(input())
T = enc(input())

psumS = [0] + list(accumulate(S))
psumT = [0] + list(accumulate(T))

q = read()
for _ in range(q):
  a, b, c, d = reads()
  ms = psumS[b] - psumS[a-1]
  mt = psumT[d] - psumT[c-1]
  ans = (ms - mt) % 3 == 0
  print("YES" if ans else "NO")