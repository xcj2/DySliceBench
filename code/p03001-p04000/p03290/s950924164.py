from sys import exit, setrecursionlimit, stderr
from functools import reduce
from itertools import *
from collections import defaultdict
from bisect import bisect
 
def read():
  return int(input())
 
def reads():
  return [int(x) for x in input().split()]

D, G = reads()
p = [0] * D; c = [0] * D
for i in range(D):
  p[i], c[i] = reads()

def subsets(s):
  return 

def divceil(a, b):
  return (a + b - 1) // b

ans = sum(p)
for sub in chain(*(combinations(range(D), r) for r in range(D))):
  rest = G - sum((i+1) * 100 * p[i] + c[i] for i in sub)
  k = max(set(range(D)).difference(sub))
  if rest <= p[k] * (k+1) * 100:
    n = max(divceil(rest, (k+1) * 100), 0)
    ans = min(ans, sum(p[i] for i in sub) + n)
print(ans)

