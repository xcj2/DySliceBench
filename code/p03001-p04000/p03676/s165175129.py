from sys import exit, setrecursionlimit, stderr
from functools import reduce
from itertools import *
from collections import *
from bisect import bisect
from heapq import *

def read():
  return int(input())
 
def reads():
  return [int(x) for x in input().split()]

MOD = 10**9 + 7
 
N = read()
A = reads()

fact = [1] * N
for i in range(1, N):
  fact[i] = (fact[i-1] * i) % MOD 
invfact = [0] * N; invfact[-1] = pow(fact[-1], MOD-2, MOD)
for i in range(N-2, -1, -1):
  invfact[i] = invfact[i+1] * (i+1) % MOD
def comb(n, k):
  return fact[n] * invfact[n-k] * invfact[k] % MOD  

cnt = Counter(A)
q = next(i for i in range(1,N+1) if cnt[i] == 2)
i1 = A.index(q); i2 = A.index(q, i1+1)
m = N - (i2 - i1)
# print(m)

print(N)
for k in range(2, N+1):
  ans = comb(N-1, k-1) * 2 + comb(N-1, k-2)
  if m >= k-1:
    ans -= comb(m, k-1)
  if k <= N-1:
    ans += comb(N-1, k)
  print(ans % MOD)
print(1)