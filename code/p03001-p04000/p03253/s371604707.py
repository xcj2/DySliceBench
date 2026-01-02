def prime_decomposition(n):
  i = 2
  d = {}
  while i * i <= n:
    while n % i == 0:
      n /= i
      if i not in d:
          d[i] = 0
      d[i] += 1
    i += 1
  if n > 1:
    if n not in d:
        d[n] = 1
  return d

def egcd(a, b):
    (x, lastx) = (0, 1)
    (y, lasty) = (1, 0)
    while b != 0:
        q = a // b
        (a, b) = (b, a % b)
        (x, lastx) = (lastx - q * x, x)
        (y, lasty) = (lasty - q * y, y)
    return (lastx, lasty, a)

# ax ≡ 1 (mod m)
def modinv(a, m):
    (inv, q, gcd_val) = egcd(a, m)
    return inv % m

def modfact(n,N):
    r = 1
    for i in range(1,n+1):
        r = r % N * i % N
    return r


def modconb(n,r,N):
    p = modfact(n,N)
    q1 = modinv(modfact(r,N),N)
    q2 = modinv(modfact(n-r,N),N)
    return p*q1%N*q2%N


N,M = map(int,input().split())
R = 10**9+7

d = prime_decomposition(M)
ans = 1
for p in d:
    ans *= modconb(d[p]+N-1,N-1,R)
    ans %= R
print(ans)
