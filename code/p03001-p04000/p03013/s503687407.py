N,M=map(int,input().split())
mod = 10**9+7
fram = [1]
for i in range(1,N+1):
  fram.append(fram[-1]*i%mod)

#def framod(n, mod, a=1):
#    for i in range(1,n+1):
#        a = a * i % mod
#    return a

def power(n, r, mod):
    if r == 0: return 1
    if r%2 == 0:
        return power(n*n % mod, r//2, mod) % mod
    if r%2 == 1:
        return n * power(n, r-1, mod) % mod

def comb(n, k, mod):
    a=fram[n]
    b=fram[k]
    c=fram[n-k]
    return (a * power(b, mod-2, mod) * power(c, mod-2, mod)) % mod

def cnt(n):
  s = sum([comb(n-i,i,mod)%mod for i in range(n//2+1)])
  s = s%mod
  return s

A0 = 0
ans = 1
for i in range(M):
  A1 = int(input()) - 1
  ans = (ans * cnt(A1-A0))%mod
  A0 = A1+2
ans = (ans * cnt(N-A0))%mod
print(ans)