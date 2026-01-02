from itertools import *
from collections import *
from functools import *

def isqrt(n):
  if n > 0:
    x = 1 << (n.bit_length() + 1 >> 1)
    while True:
      y = (x + n // x) >> 1
      if y >= x:
        return x
      x = y
  elif n == 0:
    return 0
  else:
    raise ValueError

def qrime():
  yield from [2, 3, 5, 7]
  q = [i for i in range(1, 210, 2) if 0 not in (i%3, i%5, i%7)]
  yield from q[1:]
  for i in count(210, 210):
    for j in q:
      yield i + j

def factor(n):
  p = Counter()
  limit = isqrt(n)
  for q in qrime():
    if q > limit:
      break
    while n % q ==0:
      p[q] += 1
      n //= q
    if q in p:
      limit = isqrt(n)
  if n != 1:
    p[n] += 1
  return p

def divisor(n):
  p, m = zip(*factor(n).items())
  for c in product(*map(lambda x:range(x+1), m)):
    yield reduce(int.__mul__, (x**y for x, y in zip(p, c) if y), 1)

N = int(input())
ans = reduce(int.__mul__, (c+1 for c in factor(N-1).values()), 1) - 1

for d in divisor(N):
  if d == 1:
    continue
  n = N
  while n % d == 0:
    n //= d
  if n % d == 1:
    ans += 1

print(ans)
