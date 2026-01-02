from collections import defaultdict
import sys

input = lambda: sys.stdin.readline().rstrip()

def mod_inv(a):
  x1, y1, z1 = 1, 0, a
  x2, y2, z2 = 0, 1, M
  while z1 != 1:
    d, m = divmod(z2, z1)
    x1, x2 = x2-d*x1, x1
    y1, y2 = y2-d*y1, y1
    z1, z2 = m, z1
  return x1%M

def mex(s):
  s = set(s)
  for i in range(N+1):
    if i not in s:
      return i

def calc_grundy(e):
  g = {}
  for i in range(N, 0, -1):
    if i not in e:
      continue
    m = mex(map(lambda x:g.get(x, 0), e[i]))
    if m:
      g[i] = m
  return g

def sum_grundy(grundy):
  sum_g = [defaultdict(int, {0:B_sum}) for i in range(3)]
  W, prev = B, 1
  for i in range(1, N+1):
    for s, g in zip(sum_g, grundy):
      if i in g:
        if prev != i:
          W, prev = W * pow(B, i-prev, M) % M, i
        s[g[i]] =  (s[g[i]] + W) % M
        s[0] =  (s[0] - W) % M
  return sum_g

def read_edge():
  M = int(input())
  e = defaultdict(list)
  for i in range(M):
    a, b = sorted(map(int, input().split()))
    e[a].append(b)
  return e

N = int(input())
M = 998244353
B = pow(10, 18, M)
B_sum = (pow(B, N+1, M) - B) * mod_inv(B-1) % M

edge = [read_edge() for i in range(3)]
grundy = list(map(calc_grundy, edge))
sum_g = sum_grundy(grundy)
ans = 0
for gx, sx in sum_g[0].items():
  for gy, sy in sum_g[1].items():
    gz = gx^gy
    if gz in sum_g[2]:
      ans = (ans + sx*sy*sum_g[2][gz]) % M
print(ans)
