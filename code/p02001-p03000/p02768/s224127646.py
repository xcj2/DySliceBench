n, a, b = map(int,input().split())
mod = 10 ** 9 + 7

def permutation(n,r,mod):
    perm = 1
    for integer in range(n-r+1, n+1):
        perm *= integer
        perm %= mod
    return perm

def RepeatSquaring(x, n, m):
  ans = 1
  while(n > 0):
    if(bin(n & 1) == bin(1)):
      ans = (ans*x)%m
    x = (x*x)%m
    n = n >> 1
  return ans

def cmb(n, r, mod):
    nume = permutation(n,r,mod)
    deno = permutation(r,r,mod)
    return (nume * RepeatSquaring(deno, mod-2, mod)) % mod

ans = (RepeatSquaring(2, n, mod) - 1 - cmb(n, a, mod) - cmb(n, b, mod)) % mod

print(ans)