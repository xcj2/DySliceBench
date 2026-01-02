from collections import defaultdict
import math
def factorial_memo(n, p):
  F = [1] * (n + 1)
  for i in range(n):
    F[i + 1] = F[i] * (i + 1) % p
  return F

def inverse(F, p):
  Finv = [x for x in F]
  Finv[-1] = pow(Finv[-1], p - 2, p)
  for i in range(len(F) - 2, 0, -1):
    Finv[i] = Finv[i + 1] * (i + 1) % p
  return Finv

def comb(*A):
  f = F[sum(A)]
  for a in A:
    f *= Finv[a]
  return f % p

def eratosthenes(limit):
  E = [1] * (limit + 1)
  E[0], E[1] = 0, 0
  prime_table = []
  for i, e in enumerate(E):
    if e:
      prime_table.append(i)
      for j in range(i, limit + 1, i):
        E[j] = 0
  return prime_table

N, M = map(int, input().split())
p = 10 ** 9 + 7
limit = int(math.sqrt(M)) + 1
prime_table = eratosthenes(limit)
primes = defaultdict(int)
primes[1] = 0
for prime in prime_table:
  if prime > M:
    break
  while M % prime == 0:
    primes[prime] += 1
    M //= prime
if M > 1:
  primes[M] += 1
F = factorial_memo(max(primes.values()) + N, p)
Finv = inverse(F, p)
cnt = 1
for c in primes.values():
  cnt *= comb(c, N - 1)
print(cnt % p)