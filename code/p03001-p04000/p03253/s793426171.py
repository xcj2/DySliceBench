# 素数リスト生成
def sieve(x):
    if x < 2: return []
    primes = [i for i in range(x)]
    primes[1] = 0
    for p in primes:
        if p > x ** (1/2): break
        if p == 0: continue
        for np in range(2 * p, x, p): primes[np] = 0
    return [p for p in primes if p != 0]

PS = sieve(10**6)

# 素因数分解
def factorint(x):
  d = {}
  for k in PS:
    if(x % k== 0):
      m = 1
      while(x % (k**m) == 0):
        m += 1
      d[k] = m - 1
      x = x / (k ** (m - 1))
      if x == 1:
        break
  return d

n, m = map(int, input().split())
f = factorint(m)
idx = [i for i in f.values()]
# 10^6より大きい素因数があったときの処理
re = 1
for k, v in f.items():
  re *= k**v
if m // re != 1:
  idx.append(1)


def fact(n):
  ret = 1
  for i in range(1, n + 1):
    ret *= i
  return ret
def com(n, r):
  if n - r < r: r = n - r
  ret = 1
  for i in range(n-r+1, n+1):
    ret *= i
  for j in range(1, r+1):
    ret //= j
  return ret

ans = 1
for i in range(len(idx)):
  ans *= com(idx[i] + n - 1, n - 1) % (10 ** 9 + 7)

  
print(ans % (10 ** 9 + 7))