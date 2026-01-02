#nCr % mod
def comb_mod(n, r, mod):
  x = 1
  y = 1
  for i in range(r):
    x = (x * (n - i)) % mod
    y = (y * (i + 1)) % mod
    
  ans = x * pow_k(y, mod-2, mod)
  
  return ans % mod
  
# x^n % mod
def pow_k(x, n, mod):
  if n == 0:
    return 1

  K = 1
  while n > 1:
    if n % 2 != 0:
      K = (x * K) % mod
        
    x = (x * x) % mod

    n //= 2

  return (x * K) % mod
  
def main():
  MOD = 10 ** 9 + 7
  n,k = map(int,input().split())
  
  for i in range(1,k+1):
    ans = comb_mod(n-k+1, i, MOD) * comb_mod(k-1, i-1, MOD)
    ans %= MOD
    print(ans)
    
main()