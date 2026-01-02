def factorial(n, mod=10**9+7):
    a = 1
    for i in range(1,n+1):
        a = a * i % mod
    return a


def power(n, r, mod=10**9+7):
    if r == 0: return 1
    if r%2 == 0:
        return power(n*n % mod, r//2, mod) % mod
    if r%2 == 1:
        return n * power(n, r-1, mod) % mod


def comb(n, k, mod=10**9+7):
    if n < k or k < 0:
        result = 0
    else:
        a = factorial(n, mod=mod)
        b = factorial(k, mod=mod)
        c = factorial(n-k, mod=mod)
        result = (a * power(b, mod-2, mod=mod) * power(c, mod-2, mod=mod)) % mod
    return result

n, k = map(int, input().split())
MOD = 10**9 + 7

if k >= n:
  print(comb(2*n-1, n))
  quit()

def power(n, r, mod=10**9+7):
    if r == 0: return 1
    if r%2 == 0:
        return power(n*n % mod, r//2, mod) % mod
    if r%2 == 1:
        return n * power(n, r-1, mod) % mod


fl = [-1]*(k+1)
fl[0] = 1
def f(i):
  global fl
  if fl[i] > 0: return fl[i]
  else:
    if i <= n//2:
      res = f(i-1)*(n-i+1)*(n-i)
      t = power(i, MOD-2)
      res *= t
      res %= MOD
      res *= t
      res %= MOD
      fl[i] = res
      return res
    else:
      res = f(n-i) * (n-i)
      res *= power(i, MOD-2)
      res %= MOD
      fl[i] = res
      return res


if k <= n//2:
  fl = [-1]*(k+1)
  fl[0] = 1
  def f(i):
    global fl
    if fl[i] > 0: return fl[i]
    else:
      res = f(i-1)*(n-i+1)*(n-i)
      t = power(i, MOD-2)
      res *= t
      res %= MOD
      res *= t
      res %= MOD
      fl[i] = res
      return res

  ans = 0
  for i in range(k+1):
    ans += f(i)
    ans %= MOD
else:
  fl = [-1]*(n+1)
  fl[0] = comb(n, k) * comb(n-1, k) % MOD
  def f(i):
    global fl
    if fl[i-k] > 0: return fl[i-k]
    else:
      res = f(i-1)*(n-i+1)*(n-i)
      t = power(i, MOD-2)
      res *= t
      res %= MOD
      res *= t
      res %= MOD
      fl[i-k] = res
      return res
  
  ans = 0
  for i in range(k+1, n+1):
    ans += f(i)
    ans %= MOD
  ans = comb(2*n-1, n) - ans
  ans %= MOD


print(ans % MOD)