import math
MOD = 10**9+7
def modpow(a, n, p):
  if n == 1:
    return a % p 
  elif n % 2 == 1:
    return a * modpow(a, n-1, p) % p
  else:
    return modpow(a, n//2, p) **2 % p

def I():
  return input()
def II():
  return int(input())
def MII():
  return map(int, input().split())
def LMII():
  return list(map(int, input().split()))
n,a,b = MII()
fact_a = 1
fact_n_a = 1
fact_b = 1
fact_n_b = 1
for i in range(a):
    fact_a = fact_a * (i+1) % MOD
    fact_n_a = fact_n_a * (n-a+1+i) % MOD
cmb_a = fact_n_a * modpow(fact_a, MOD-2, MOD) % MOD
for i in range(b):
    fact_b = fact_b * (i+1) % MOD
    fact_n_b = fact_n_b * (n-b+1+i) % MOD
cmb_b = fact_n_b * modpow(fact_b, MOD-2, MOD) % MOD

print((modpow(2, n, MOD)-1-cmb_a-cmb_b)%MOD)