# -*- coding: utf-8 -*-

MOD = 10**9 +7

kaijo_memo = []
def kaijo(n):
  if(len(kaijo_memo) > n):
    return kaijo_memo[n]
  if(len(kaijo_memo) == 0):
    kaijo_memo.append(1)
  while(len(kaijo_memo) <= n):
    kaijo_memo.append(kaijo_memo[-1] * len(kaijo_memo) % MOD)
  return kaijo_memo[n]

gyaku_kaijo_memo = []
def gyaku_kaijo(n):
  if(len(gyaku_kaijo_memo) > n):
    return gyaku_kaijo_memo[n]
  if(len(gyaku_kaijo_memo) == 0):
    gyaku_kaijo_memo.append(1)
  while(len(gyaku_kaijo_memo) <= n):
    gyaku_kaijo_memo.append(gyaku_kaijo_memo[-1] * pow(len(gyaku_kaijo_memo),MOD-2,MOD) % MOD)
  return gyaku_kaijo_memo[n]

def nCr(n,r):
  if(n == r):
    return 1
  if(n < r or r < 0):
    return 0
  ret = 1
  ret *= kaijo(n)
  ret %= MOD;
  ret *= gyaku_kaijo(r)
  ret %= MOD;
  ret *= gyaku_kaijo(n-r)
  ret %= MOD;
  return ret




 
n,k = map(int, input().split())
 
################
#p = 10**9 + 7
#def comb(n,k,p):
#  ans = 1
#  for i in range(1,k+1):
#    ans = ans * (n - (i-1)) % p
#    ans = ans * pow(i, p-2, p)
#  return ans
################
 
if k >= n:
  ans = nCr(2*n-1, n) % MOD
else:
  ans = 0
  for i in range(0,k+1):
    temp = (nCr(n-1, i) % MOD) * (nCr(n, i) % MOD) % MOD
    ans = (ans + temp) % MOD
    
print(ans)
