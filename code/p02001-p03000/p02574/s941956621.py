def gcd(x, y):
  b = max(x, y)
  s = min(x, y)
  r = b % s
  while r != 0:
    b = s
    s = r
    r = b % s
  return s

def lcm(x, y):
  return (x * y) // gcd(x,y)

import math
def prime(x):
  p = {}
  last = math.floor(x ** 0.5)
  if x % 2 == 0:
    cnt = 1
    x //= 2
    while x & 1 == 0:
      x //= 2
      cnt += 1
    p[2] = cnt
  for i in range(3, last + 1, 2):
    if x % i == 0:
      x //= i
      cnt = 1
      while x % i == 0:
        cnt += 1
        x //= i
      p[i] = cnt
  if x != 1:
    p[x] = 1
  return p

N = int(input())
A = list(map(int, input().split()))

R = {}
F = True
for i in A:
  p = prime(i)
  for j in p.keys():
    if j in R:
      F = False
      break
    else:
      R[j] = 1
  else:
    continue
  break

if F:
  print("pairwise coprime")
  exit()

t = A[0]
for i in range(1, N):
  t = gcd(t, A[i])

if t == 1:
  print("setwise coprime")
else:
  print("not coprime")
