def read():
  return int(input())

def reads():
  return [int(x) for x in input().split()]

P = 998244353

N, A, B, K = reads()

def inv(n):
  return pow(n, P-2, P)

fact = [1] * (N+1)
for i in range(1, N+1):
  fact[i] = fact[i-1] * i % P

invfact = [inv(fact[N])] * (N+1)
for i in range(N, 0, -1):
  invfact[i-1] = invfact[i] * i % P

def comb(n, k):
  # assert 0 <= k <= n
  return fact[n] * invfact[k] * invfact[n-k] % P

result = 0
for x in range(N+1):
  y, r = divmod(K - A * x, B)
  if r == 0 and 0 <= y <= N:
    result = result + comb(N, x) * comb(N, y) % P

print(result % P)