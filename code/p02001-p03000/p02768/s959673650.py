from sys import stdin
input = stdin.readline


def pow_k(x, n, MOD=1_000_000_007):
  if n == 0:
    return 1
  K = 1
  while n > 1:
    if n % 2 != 0:
      K *= x
      K %= MOD
    x *= x
    x %= MOD
    n //= 2
  return K * x % MOD


def comb(n, r, MOD=1_000_000_007):
  if n - r < r: r = n - r
  if r == 0: return 1
  if r == 1: return n

  numerator = [n - r + k + 1 for k in range(r)]
  denominator = [k + 1 for k in range(r)]

  for p in range(2, r+1):
    pivot = denominator[p-1]
    if pivot > 1:
      offset = (n - r) % p
      for k in range(p-1, r, p):
        numerator[k - offset] /= pivot
        denominator[k] /= pivot

  result = 1
  for k in range(r):
    if numerator[k] > 1:
      result *= int(numerator[k])
      result %= MOD

  return result


def main():
  N, a, b = list(map(int, input().split()))

  print((pow_k(2, N)-1-comb(N, a)-comb(N, b)) % 1_000_000_007)


if(__name__ == '__main__'):
  main()
