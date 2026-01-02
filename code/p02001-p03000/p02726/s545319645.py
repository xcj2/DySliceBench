from itertools import *

def loop(n):
  yield from repeat(n, (n-1)>>1)
  if n & 1 == 0:
    yield n >> 1
  yield from repeat(0)

def branch(n, l):
  if n:
    yield 0
    a, b = divmod(l-3, 2)
    s = 1
    for i in range(n+a+b):
      yield s
      if i < a:
        s += 2
      elif b and i==a:
        s += 1
      if n <= i:
        s -= 2
      elif i==n-1:
        s -= 1
  yield from repeat(0)

def b_to_b(n):
  yield n
  yield from range(n, 0, -1)
  yield from repeat(0)

N, X, Y = map(int, input().split())
L = Y - X + 1
for p in islice(zip(loop(L), branch(X-1, L), branch(N-Y, L), b_to_b(N-L)), N-1):
  print(sum(p))
