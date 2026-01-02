import math

X, Y = input().split(" ")
X, Y = int(X), int(Y)

comb_list = {}
mod_param = 10**9 + 7

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

def comb(a, b):
  ans = 1
  for i in range(b+1, a+1):
    ans *= i
    ans %= mod_param
  for i in range(1, a-b+1):
    k = modinv(i, mod_param)
    ans *= k
    ans %= mod_param
  return ans

if (abs(2*X-Y)%3 != 0):
  print(0)
else:
  alpha = (2*Y-X)//3
  beta = (2*X-Y)//3
  if alpha > beta:
    print(comb(alpha+beta, beta))
  else:
    print(comb(alpha+beta, alpha))
