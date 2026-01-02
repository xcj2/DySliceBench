def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    divisors.sort()
    return divisors

def nasu(x):
  t = make_divisors(x)
  c = 0
  for i in t:
    c += D[i]
  return c

def honya(x):
  y = 0
  k = 1
  for i in range(x - 1, -1, -1):
    if X[i]:
      y = (y + k) % MOD
    k = (k * 2) % MOD
  return y + honyaraka(x)

def honyaraka(x):
  cnt = 0
  for i in range(N // x):
    t = i % 2
    for j in range(x):
      if X[cnt] != (X[j] ^ t):
        if X[cnt] == 0:
          return 0
        else:
          return 1
      cnt += 1
  return 1


N = int(input())
X = list(map(int, input()))
MOD = 998244353

Y = 0
k = 1
for i in range(N - 1, -1, -1):
  if X[i]:
    Y = (Y + k) % MOD
  k = (k * 2) % MOD

D = [0] * (N + 1)
L = make_divisors(N)

cnt = 0
for i in L:
  if i != N and (N // i) % 2 == 1:
    D[i] = honya(i) - nasu(i)
    cnt += D[i]

D[N] = Y - cnt + 1

ans = 0
for i in L:
  ans = (ans + D[i] * i * 2) % MOD

print(ans)