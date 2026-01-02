import cmath
pi = cmath.pi

def expD(t):
  nexp, pexp = {}, {}
  while t != 0:
    pexp[t] = cmath.exp(2j*pi/t)
    nexp[t] = cmath.exp(-2j*pi/t)
    t //= 2
  return nexp, pexp
def powerlimit(x):
  a = 1
  while a < x:
    a *= 2
  return a

N, M = map(int, input().split())
A = list(map(int, input().split()))
m = max(A)
X = [0 for i in range(m+1)]
for i in A:
  X[i] += 1
limit = powerlimit(2*(m+1))
X = X[:] + [0 for _ in range(limit-m-1)]

nexp, pexp = expD(limit)

def fft(f, n):
  hn = n//2
  if n == 1:
    return f
  elif n == 2:
    return [f[0] + f[1], f[0] - f[1]]
  else:
    f0 = [f[2*_] for _ in range(hn)]
    f1 = [f[2*_+1] for _ in range(hn)]
    f0 = fft(f0, hn)
    f1 = fft(f1, hn)
    grow = 1
    fund = nexp[n]
    for i in range(hn):
      right = grow * f1[i]
      f[i] = f0[i] + right
      f[i+hn] = f0[i] - right
      grow *= fund
    return f
def ifft(f, n):
  hn = n//2
  if n == 1:
    return f
  elif n == 2:
    return [f[0] + f[1], f[0] - f[1]]
  else:
    f0 = [f[2*_] for _ in range(hn)]
    f1 = [f[2*_+1] for _ in range(hn)]
    f0 = ifft(f0, hn)
    f1 = ifft(f1, hn)
    grow = 1
    fund = pexp[n]
    for i in range(hn):
      right = grow * f1[i]
      f[i] = f0[i] + right
      f[i+hn] = f0[i] - right
      grow *= fund
    return f
  
F = fft(X, limit)
V = [F[i]*F[i] for i in range(limit)]
E = ifft(V, limit)
for i in range(limit):
  E[i] = int(0.5+E[i].real/limit)
cnt = 0
S = 0
point = limit - 1

while cnt < M:
  Ep = E[point]
  if Ep != 0:
    if cnt + Ep > M:
      S += (M - cnt) * point
      cnt = M
    else:
      S += point * Ep
      cnt += Ep
  point -= 1
print(S)
