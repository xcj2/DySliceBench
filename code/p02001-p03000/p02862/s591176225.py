x, y = map(int, input().split())
mod = 10**9+7 
def check(x, y):
  if (2*y-x)/3 < 0 or (2*x -y)/3 < 0:
    return False
  if (x+y)%3 != 0:
    return False
  return True

def modPow(a, n, mod):
  if n == 1:
    return a % mod
  if n%2 == 1:
    return (a * modPow(a, n - 1, mod)) % mod
  t = modPow(a, n / 2, mod)
  return (t * t) % mod

def comb(n, r, mod):
    r = min(r, n-r)
    x, y  = 1, 1
    for i in range(1, r+1):
      y =  y* i % mod
      x =  x* (n+1-i) % mod
    return x * modPow(y, mod-2, mod) % mod
  
if check(x, y):
  print(comb((2*y-x)//3+(2*x -y)//3, (2*y-x)//3, mod))
else:
  print(0)