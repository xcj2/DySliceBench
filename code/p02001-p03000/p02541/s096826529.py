import sys
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]  

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

# return [g, x, y]
# g = gcd(a, b)
# x, y satisfies a x + b y = g
def extgcd(a, b):
    if b == 0:
        return [a, 1, 0]
    g, x, y = extgcd(b, a%b)
    return [g, y, x - a//b * y]

# eq0: x = a0 (mod m0)
# eq1: x = a1 (mod m1)
# returns [xt, mod] such that x = xt + k mod for integer k.
def crt(eq0, eq1):
    a0, m0 = eq0
    a1, m1 = eq1

    g = gcd(m0, m1)

    if a0 % g != a1 % g:
        return [-1, -1]
        #raise Exception("x doesn't exist.")

    if g > 1:
        m0 //= g
        m1 //= g

        while True:
            gt = gcd(m0, g)
            if gt == 1:
                break
            m0 *= gt
            g //= gt
        
        m1 *= g

        a0 %= m0
        a1 %= m1

    g, p, q = extgcd(m0, m1)
    
    x = a0 * q * m1 + a1 * p * m0
    mod = m0 * m1
    x = x % mod

    return [x, mod]

# 本処理
N = int(input())
divs = make_divisors(2*N)
"""
if N == 1:
  print(1)
  sys.exit()
"""

ans = INF = 10**20
for x in divs:
  y = 2*N // x
  xt, mod = crt([0,x], [-1,y])
  if x == 2*N or xt == -1:
    continue
  #print(x, y, xt)
  ans = min(ans, xt)
  
print(ans)
    
  

  