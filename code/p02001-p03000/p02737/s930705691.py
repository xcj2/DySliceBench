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
  for i in range(N+1):
    if i not in s:
      return i

def calc_grundy(edge):
  grundy = [{} for i in range(3)]
  sum_g = [defaultdict(int, {0:W_sum}) for i in range(3)]
  W = W_last
  for i in range(N, 0, -1):
    for g, s, e in zip(grundy, sum_g, edge):
      if i in e:
        m = mex({g.get(j, 0) for j in e[i]})
        if m:
          g[i] = m
          s[g[i]] =  (s[g[i]] + W) % M
          s[0] =  (s[0] - W) % M
    W = W * B_inv % M
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
B_inv = mod_inv(B)
W_last = pow(B, N, M)
W_sum = (W_last - 1) * B * mod_inv(B-1) % M

edge = [read_edge() for i in range(3)]
sum_g = calc_grundy(edge)
ans = 0
for gx, sx in sum_g[0].items():
  for gy, sy in sum_g[1].items():
    gz = gx^gy
    sz = sum_g[2][gz]
    if sz:
      ans = (ans + sx*sy*sz) % M
print(ans)
