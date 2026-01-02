from collections import defaultdict
n = int(input())
if n < 10:
  print(0)
  exit()
  
def gcd(a, b):
    while b: a, b = b, a % b
    return a
def isPrimeMR(n):
    d = n - 1
    d = d // (d & -d)
    L = [2]
    for a in L:
        t = d
        y = pow(a, t, n)
        if y == 1: continue
        while y != n - 1:
            y = (y * y) % n
            if y == 1 or t == n - 1: return 0
            t <<= 1
    return 1
def findFactorRho(n):
    m = 1 << n.bit_length() // 8
    for c in range(1, 99):
        f = lambda x: (x * x + c) % n
        y, r, q, g = 2, 1, 1, 1
        while g == 1:
            x = y
            for i in range(r):
                y = f(y)
            k = 0
            while k < r and g == 1:
                ys = y
                for i in range(min(m, r - k)):
                    y = f(y)
                    q = q * abs(x - y) % n
                g = gcd(q, n)
                k += m
            r <<= 1
        if g == n:
            g = 1
            while g == 1:
                ys = f(ys)
                g = gcd(abs(x - ys), n)
        if g < n:
            if isPrimeMR(g): return g
            elif isPrimeMR(n // g): return n // g
            return findFactorRho(g)
def primeFactor(n):
    i = 2
    ret = {}
    rhoFlg = 0
    while i * i <= n:
        k = 0
        while n % i == 0:
            n //= i
            k += 1
        if k: ret[i] = k
        i += i % 2 + (3 if i % 3 == 1 else 1)
        if i == 101 and n >= 2 ** 20:
            while n > 1:
                if isPrimeMR(n):
                    ret[n], n = 1, 1
                else:
                    rhoFlg = 1
                    j = findFactorRho(n)
                    k = 0
                    while n % j == 0:
                        n //= j
                        k += 1
                    ret[j] = k
 
    if n > 1: ret[n] = 1
    if rhoFlg: ret = {x: ret[x] for x in sorted(ret)}
    return ret
  
d = defaultdict(int)
for i in range(2,n+1):
  f = primeFactor(i)
  for j,k in f.items():
    d[j] += k

lim_74 = -1
lim_24 = -1
lim_14 = -1
lim_4 = -1
lim_2 = -1
cnt = 0
for i in d.values():
  if lim_74 == -1 and i < 74:
    lim_74 = cnt
  if lim_24 == -1 and i < 24:
    lim_24 = cnt
  if lim_14 == -1 and i < 14:
    lim_14 = cnt
  if lim_4 == -1 and i < 4:
    lim_4 = cnt
  if lim_2 == -1 and i < 2:
    lim_2 = cnt
    break
  cnt += 1
  
ans = lim_74
ans += lim_24*(lim_24-1)
ans += lim_14*(lim_14-1)
ans += lim_24*(lim_2-lim_24)
ans += lim_14*(lim_4-lim_14)
ans += lim_4*(lim_4-1)*(lim_4-2)//2
ans += lim_4*(lim_4-1)*(lim_2-lim_4)//2
print(ans)