def inv_gcd(a, b):
    a = (a + b) % b
    if a == 0:
        return (b, 0)
    s, t = b, a
    m0, m1 = 0, 1
 
    while t:
        u = s // t
        s -= t * u
        m0 -= m1 * u
 
        tmp = s
        s = t
        t = tmp
        tmp = m0
        m0 = m1
        m1 = tmp
    
    if m0 < 0:
        m0 += b // s
    return (s, m0)
 
 
def crt(r, m):
    n = len(r)
    r0, m0 = 0, 1
 
    for i in range(n):
        r1, m1 = (r[i] + m[i]) % m[i], m[i]
 
        if m0 < m1:
            m0, m1 = m1, m0
            r0, r1 = r1, r0
        
        if m0 % m1 == 0:
            if r0 % m1 != r1:
                return (0, 0)
            continue
        
        g, im = inv_gcd(m0, m1)
 
        u1 = m1 // g
        if (r1 - r0) % g:
            return (0, 0)
        
        x = (r1 - r0) // g % u1 * im % u1
 
        r0 += x * m0
        m0 *= u1
        if (r0 < 0):
            r0 += m0
        
    return (r0, m0)


def divisors(n):
  divisors = []
  for i in range(1, int(n**0.5)+1):
    if n % i == 0:
      divisors.append(i)
      if i != n // i:
        divisors.append(n//i)
  divisors.sort()
  return divisors


# print(divisors(z))

z=int(input())


ans = z-1 if z%2 else 2*z-1
for i in divisors(2*z):
  y=2*z//i
  if y == 1:
    continue
  a=[0,-1]
  b=[i,y]
  rem, mod = crt(a, b)
  #print(rem)
  #print(mod)
  if rem == mod == 0:
      continue
  ans = min(ans, rem)

print(ans if z-1 else 1)