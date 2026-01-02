def framod(n, mod, a=1):
    for i in range(1,n+1):
        a=a * i % mod
    return a

def power(n, r, mod):
    if r == 0: return 1
    if r%2 == 0:
        return power(n*n % mod, r//2, mod) % mod
    if r%2 == 1:
        return n * power(n, r-1, mod) % mod

def comb(n, k, mod):
    a=framod(n, mod)
    b=framod(k, mod)
    c=framod(n-k, mod)
    return (a * power(b, mod-2, mod) * power(c, mod-2, mod)) % mod


X, Y = map(int, input().split())
mod = 10**9 + 7

if (X + Y)%3 != 0:
  result = 0
else:
  n1 = (2*Y - X)//3
  n2 = (2*X - Y)//3
  if n1 < 0 or n2 < 0:
    result = 0
  else:
    result = comb(n1+n2, n1, mod)

print(result)
    