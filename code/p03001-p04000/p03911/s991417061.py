from sys import exit, setrecursionlimit
from functools import reduce
from itertools import *
from collections import defaultdict
from bisect import bisect

def read():
  return int(input())

def reads():
  return [int(x) for x in input().split()]

setrecursionlimit(1000000)

(N, M) = reads()

d = defaultdict(list)
V = set()

for i in range(N):
  V.add(("p", i+1))
for j in range(M):
  V.add(("l", j+1))

for i in range(1, N+1):
  Ls = reads()[1:]
  for j in Ls:
    d[("l", j)].append(("p", i))
    d[("p", i)].append(("l", j))

def walk(v):
  V.discard(v)
  for w in d[v]:
    if w in V:
      walk(w)

# for (k, v) in d.items():
#   print(k, v)

v = ("p", 1)
walk(v)

# print(V)

print("NO" if len([v for v in V if v[0] == "p"]) > 0 else "YES")
