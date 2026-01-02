from collections import defaultdict

M = 998244353
B = pow(10, 18, M)
N = int(input())

def ext_euc(a, b):
  x1, y1, z1 = 1, 0, a
  x2, y2, z2 = 0, 1, b
  while z1 != 1:
    d, m = divmod(z2,z1)
    x1, x2 = x2-d*x1, x1
    y1, y2 = y2-d*y1, y1
    z1, z2 = m, z1
  return x1, y1

def inv_mod(a, b, m):
  x, y = ext_euc(a, m)
  return (x * b % m)

def mex(s):
  for i in range(N+1):
    if i not in s:
      return i

def calc_grundy(e):
  g = {}
  sum_g = defaultdict(int)
  sum_g[0] = inv_mod(B-1, pow(B, N+1, M)-B, M)
  for i in range(N, 0, -1):
    if i not in e:
      continue
    m = mex({g.get(j, 0) for j in e[i]})
    if m:
      g[i] = m
      x = pow(B, i, M)
      sum_g[m] += x
      sum_g[0] -= x
  return sum_g

def read_edge():
  M = int(input())
  e = defaultdict(set)
  for i in range(M):
    a, b = sorted(map(int, input().split()))
    e[a].add(b)
  return e

def solve(N, edge):
  sum_g = list(map(calc_grundy, edge))
  ret = 0
  for gx, sx in sum_g[0].items():
    for gy, sy in sum_g[1].items():
      gz = gx^gy
      sz = sum_g[2][gz]
      if sz:
        ret += (sx*sy*sz) % M
  return ret%M


edge = [read_edge() for i in range(3)]

print(solve(N, edge))