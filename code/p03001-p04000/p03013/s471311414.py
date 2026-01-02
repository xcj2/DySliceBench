import sys
n, m = map(int, input().split())
danger = [int(input()) for i in range(m)]

MOD = 1000000007
MAX = 200000           #適当な数を入力
fac, finv, inv = [[0]*MAX for i in range(3)]
def combinit():     #MAXまでの下準備
  fac[0] = fac[1] = 1
  finv[0] = finv[1] = 1
  inv[1] = 1
  for i in range(2, MAX):
    fac[i] = fac[i - 1] * i % MOD
    inv[i] = MOD - inv[MOD%i] * (MOD // i) % MOD
    finv[i] = finv[i - 1] * inv[i] % MOD

def modcomb(n, k):      #mod(nCk)を計算、ただしn<MAX
  if (n < k):
    return 0
  if (n < 0 or k < 0):
    return 0
  return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD
combinit()          #下準備の実行 O(MAX)

def poss(n):
  n -= 1
  k = n//2
  ans = 0
  for i in range(k+1):
    ans += modcomb(n-i, i) % MOD
  return ans % MOD
if m == 0:
  print(poss(n+1))
  sys.exit()
ans = poss(danger[0])
for i in range(1, m):
  if danger[i] - danger[i-1] == 1:
    print(0)
    sys.exit()
  ans *= poss(danger[i] - danger[i-1] - 1)
  ans = ans % MOD
ans *= poss(n - danger[m-1])

print(ans % MOD)

