n, k = map(int, input().split())
l = list(map(int, input().split()))
l.sort()

MOD = 1000000007

def mod(n):         
  return n % MOD

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

lst = [0]
for i in range(n):
  lst.append(lst[i]+l[i])

ans = 0
for i in range(n-k+1):
  ans += mod(lst[n] - lst[i+k-1] - lst[n-k-i+1])*modcomb(k+i-2, k-2) % MOD
  
print(mod(ans))