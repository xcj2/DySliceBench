def ints():
  return [int(x) for x in input().split()]
def readi():
  return int(input())
X, Y = ints()

start = (0, 0)
end = (X, Y)
memo = {}
MOD = 10**9+7
N = 10**6+1
fact = [None]*N
fact[0] = 1
for i in range(1, N):
  fact[i] = fact[i-1]*i % MOD

def no():
  print(0)
  exit()

def inv(x):
  res = 1
  k = MOD-2
  y = x
  while k>0:
    if k%2==1:
      res = (res * y) % MOD
    y = (y * y) % MOD
    k //= 2
  return res

def C(n, k):
  a = fact[n]
  b = fact[k]
  c = fact[n-k]
  bc = (b*c) % MOD

  return (a * inv(bc)) % MOD

x = X+Y
y = -X+Y

if x%3>0:
  no()

xn = x//3
yn= (y+xn)//2
if yn<0 or yn>xn:
  no()
print(C(xn, yn))
