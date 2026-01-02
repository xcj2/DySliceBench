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
    f %= p
  return f
 
N, K = map(int, input().split())
p = 10 ** 9 + 7
F = factorial_memo(N, p)
Finv = inverse(F, p)
 
for i in range(1, K + 1):
  base = comb(K - i, i - 1)
  if N - K - i + 1 >= 0:
    multi = comb(i, N - K - i + 1)
  else:
    multi = 0
  print((base * multi) % p)