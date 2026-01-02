import sys
n, m, k = map(int, input().split())
prime_mod = 998244353

def prime_cycle_division(a, b):
  inverted = pow(b, prime_mod-2, prime_mod)
  return (a*inverted)%prime_mod

def gen_mod_combs(places):
  k = 0
  x = 1
  while True:
    yield x
    factor = prime_cycle_division(places-k, k+1)
    x = (x*factor)%prime_mod
    k += 1

def combos(j):
  ans = (m*next(gen))%prime_mod
  ans = (ans*pow(m-1, n-1-j, prime_mod))%prime_mod
  return ans

total = 0
gen = gen_mod_combs(n-1)
for j in range(k+1):
  total = (total + combos(j))%prime_mod
print(total)