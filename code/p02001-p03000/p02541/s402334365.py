def floor_sum(n, m, a, b):
    res = 0
    while True:
        if a >= m:
            res += (n - 1) * n * (a // m) // 2
            a %= m
        if b >= m:
            res += n * (b // m)
            b %= m
        y_max = (a * n + b) // m
        if y_max == 0: break
        x_max = b - y_max * m
        res += (n + x_max // a) * y_max
        n, m, a, b = y_max, a, m, x_max % a
    return res

def inv_gcd(a, b):
    a %= b
    if a == 0: return b, 0
    s = b
    t = a
    m0 = 0
    m1 = 1
    while t:
        u = s // t
        s -= t * u
        m0 -= m1 * u
        s, t = t, s
        m0, m1 = m1, m0
    if m0 < 0: m0 += b // s
    return s, m0

def inv_mod(x, m):
    assert 1 <= m
    g, im = inv_gcd(x, m)
    assert g == 1
    return im


def f(x):
  r=[]
  for i in range(2,int(x**0.5)+1):
    if x%i==0:
      r.append([i,0])
      while x%i==0:
        x//=i
        r[-1][1]+=1
  if x!=1:
    r.append([x,1])
  return r

def crt(r, m):
    assert len(r) == len(m)
    n = len(r)
    r0 = 0
    m0 = 1
    for i in range(n):
        assert 1 <= m[i]
        r1 = r[i] % m[i]
        m1 = m[i]
        if m0 < m1:
            r0, r1 = r1, r0
            m0, m1 = m1, m0
        if m0 % m1 == 0:
            if r0 % m1 != r1: return 0, 0
            continue
        g, im = inv_gcd(m0, m1)
        u1 = m1 // g
        if (r1 - r0) % g: return 0, 0
        x = (r1 - r0) // g * im % u1
        r0 += x * m0
        m0 *= u1
        if (r0 < 0): r0 += m0
    return r0, m0

N=int(input())
X=f(N*2)
if len(X)==1:
  print(2*N-1)
  exit()
X2=[X[i][0]**X[i][1] for i in range(len(X))]
Y=[1]
for i in range(len(X)):
  Y.append(Y[i]*X2[i])
P=10**20
M=len(Y)-1
for i in range(1,(1<<M)-1):
  A=[((i&(1<<j))>>j) for j in range(M)]
  P=min(P,crt(A,X2)[0])
print(P-1)