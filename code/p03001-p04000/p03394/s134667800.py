from sys import exit, setrecursionlimit, stderr
from functools import reduce
from itertools import *
from collections import *
from bisect import bisect
 
def read():
  return int(input())
 
def reads():
  return [int(x) for x in input().split()]

ls = [n for n in range(2,30001) if n % 2 == 0 or n % 3 == 0]

def gcd(x, y):
  return x if y == 0 else gcd(y, x % y)

def check(N, ans):
  assert len(ans) == len(set(ans)) == N
  S = sum(ans)
  assert reduce(gcd, ans) == 1
  assert all(gcd(S - a, a) != 1 for a in ans)

def solve(N):
  if N == 3:
    return [2, 5, 63]
  q, r = divmod(N, 8)
  t = q * 8
  ans = ls[:t]
  if r % 2 == 1:
    ans += [ls[t+3]]
  r //= 2
  if r == 1:
    ans += [ls[t], ls[t+2]]
  elif r == 2:
    ans += ls[t:t+3] + [ls[t+5]]
  elif r == 3:
    ans += ls[t:t+3] + ls[t+4:t+7]
  return ans

# for N in range(3, 100):
#   ans = solve(N)
#   print(N, ans, file=stderr)
#   check(N, ans)

N = read()
print(' '.join(str(a) for a in solve(N)))