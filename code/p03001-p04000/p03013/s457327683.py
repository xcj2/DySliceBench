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

fn = [1, 1]
for i in range(10 ** 5):
  fn1 = fn[-2] + fn[-1]
  fn.append(fn1)

n, m = map(int, input().split())
an = []
for _ in range(m):
  an.append(int(input()))
an.append(n+1)

now = 0
pattern = 1
for a in an:
  if now >= a:
    pattern = 0
    break
  steps = a - now - 1
  pattern = mul(pattern, fn[steps])
  now = a + 1

print(pattern)
  
  