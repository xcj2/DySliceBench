import sys

readline = sys.stdin.readline

ns = lambda: readline().rstrip()
ni = lambda: int(readline().rstrip())
nm = lambda: map(int, readline().split())
nl = lambda: list(map(int, readline().split()))

def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int((n+1)**0.5)+1):
        if is_prime[i]:
            for j in range(i *2, n + 1, i):
                is_prime[j] = False
    res = [i for i in range(n+1) if is_prime[i]]
    return res

def make_modinv_list(n, mod=10**9+7):
    inv_list = [0]*(n+1)
    inv_list[1] = 1
    for i in range(2, n+1):
        inv_list[i] = (mod - mod//i * inv_list[mod%i] % mod)
    return inv_list

def solve():
  mod = 998244353
  n = ni()
  a = nl()
  m = max(a)
  s = -sum(a) % mod
  l = [0]*(m+1)
  for x in a:
    l[x] += x
  a = make_modinv_list(m, mod)
  pr = primes(m) 
  for i in pr:
    for j in range(m//i, 0, -1):
      l[j] += l[j*i]
  for i in range(m+1):
    l[i] = l[i] * l[i] % mod
  for i in pr:
    for j in range(1, m//i + 1):
      l[j] = (l[j] - l[j*i]) % mod
  for i in range(1, m+1):
    if l[i]:
      s = (s + l[i] * a[i]) % mod
  print(s * a[2] % mod)
  return

solve()
