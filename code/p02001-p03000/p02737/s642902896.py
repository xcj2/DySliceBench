from collections import defaultdict

M = 998244353
B = 10**18 % M

def mex(s):
  for i in range(max(s)+2):
    if i not in s:
      return i

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

def calc_grundy(e):
  g = {}
  sum_g = defaultdict(int)
  sum_g[0] = inv_mod(B-1, pow(B, N+1, M)-B, M)
  for i in sorted(e.keys(), reverse=True):
    m = mex({g.get(j,0) for j in e[i]})
    if m:
      g[i] = m
      x = pow(B, i, M)
      sum_g[m] += x
      sum_g[0] -= x
  return sum_g

def get_edge():
  M = int(input())
  e = defaultdict(set)
  for i in range(M):
    a, b = sorted(map(int, input().split()))
    e[a].add(b)
  return e

def solve(N, edge):
  sum_g = list(map(calc_grundy, edge))
  ret = 0
  for gx, x in sum_g[0].items():
    for gy, y in sum_g[1].items():
      gz = gx^gy
      z = sum_g[2][gz]
      ret = (ret + x*y*z)%M
  return ret

N = int(input())
edge = [get_edge() for i in range(3)]

print(solve(N, edge))