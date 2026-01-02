from itertools import *
from collections import *
from math import *
def qrime():
  p = [2, 3, 5, 7]
  yield from p
  q = [i for i in range(1, 210, 2) if 0 not in (i%3, i%5, i%7)]
  yield from q[1:]
  for i in count(210, 210):
    for j in q:
      yield i + j

def factor(n):
  limit = int(sqrt(n))
  p = Counter()
  for q in qrime():
    if n == 1 or q > limit:
      break
    while n % q ==0:
      p[q] += 1
      n //= q
      limit = int(sqrt(n))
  if n != 1:
    p[n] += 1
  return p

def divisor(n):
  f = factor(n)
  p, m = zip(*f.items())
  for c in product(*map(lambda x:range(x+1), m)):
    if sum(c) == 0:
      continue
    C = 1
    for a, b in zip(p, c):
      C *= pow(a, b)
    yield C

ans = 0
N = int(input())
for d in divisor(N):
  n = N
  while n % d == 0:
    n //= d
  if n % d == 1:
    ans += 1

f = factor(N-1)
ans2 = 1
for c in f.values():
  ans2 *= c+1

print(ans + ans2 - 1)