import sys
input = sys.stdin.readline
from itertools import accumulate
n = int(input())
m = (n*(n+1)//2+1)//2
U = 2**20
A = tuple(map(int, input().split()))
def test(x):
  L = [0] + list(accumulate((-1)**(a<x) for a in A))
  B = [0]*(U+1)
  def add(i):
    while i<=U:
      B[i] += 1
      i += i & -i
  def acc(i):
    res = 0
    while i:
      res += B[i]
      i -= i & -i
    return res
  cnt = 0
  for l in L:
    cnt += acc(l+n+5)
    add(l+n+5)
  return cnt >= m
ok = 0
ng = 10**9+1
while ng - ok > 1:
  mid = (ng+ok)//2
  if test(mid):
    ok = mid
  else:
    ng = mid
print(ok)