MOD = 10 ** 9 + 7
def add(a, b):
  return (a + b) % MOD
def sub(a, b):
  return (a - b) % MOD
def mul(a, b):
  return ((a % MOD) * (b % MOD)) % MOD
def div(a, b):
  return ( (a % MOD) * (power(b, MOD)) ) % MOD
def power(a, b):
  return pow(a, b, MOD)


n, k = map(int, input().split())
an = list(map(int, input().split()))
n1 = [0] * n
n2 = [0] * n
for i, v in enumerate(an):
  n1[i] = len([x for x in an[i+1:] if x < v])
  n2[i] = n1[i] + len([x for x in an[:i] if x < v])

cnt = 0
ks = (k-1) * k // 2
for i in range(n):
  cnt = add(cnt, mul(n1[i], k))
  cnt = add(cnt, mul(n2[i], ks))
print(cnt)