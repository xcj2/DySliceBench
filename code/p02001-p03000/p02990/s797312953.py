MOD = pow(10, 9) + 7

fac = [0 for _ in range(2050)]
finv = [0 for _ in range(2050)]
inv = [0 for _ in range(2050)]

def COMinit():
  fac[0] = 1
  fac[1] = 1
  finv[0] = 1
  finv[1] = 1
  inv[1] = 1
  for i in range(2, 2050):
    fac[i] = fac[i-1] * i % MOD
    inv[i] = MOD - inv[MOD%i] * (MOD//i) % MOD
    finv[i] = finv[i-1] * inv[i] % MOD


def COM(n, k):
  if n < k:
    return 0
  if n < 0 or k < 0:
    return 0
  return fac[n] * (finv[k] * finv[n-k] % MOD) % MOD


def main():
  COMinit()
  n, k = map(int, input().split())
  for i in range(1, k+1):
    if n - k + 1 >= i:
      print(COM(n-k+1, i) * COM(k-1, i-1) % MOD)
    else:
      print(0)


if __name__ == '__main__':
  main()
