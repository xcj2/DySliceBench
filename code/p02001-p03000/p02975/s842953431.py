from sys import exit, setrecursionlimit, stderr
from functools import reduce
from itertools import *
from collections import defaultdict, Counter
from bisect import bisect

setrecursionlimit(10**6)

def read():
  return int(input())

def reads():
  return [int(x) for x in input().split()]

def answer(b):
  print("Yes" if b else "No")
  exit()

N = read()
a = reads()

d = Counter(a)
keys = list(d.keys())
keys.sort()

if len(keys) > 3:
  answer(False)

if len(keys) == 1:
  answer(keys[0] == 0)
elif len(keys) == 2:
  if keys[0] != 0:
    answer(False)
  v = keys[1]
  answer(d[0] * 2 == d[v])
else:
  assert len(keys) == 3
  v, w, x = keys
  if v ^ w == x and d[v] == d[w] == d[x]:
    answer(True)
  else:
    answer(False)

