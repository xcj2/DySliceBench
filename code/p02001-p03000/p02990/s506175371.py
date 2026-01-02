def framod(n, mod=10**9+7, a=1):
    for i in range(1,n+1):
        a=a * i % mod
    return a


def power(n, r, mod=10**9+7):
    if r == 0: return 1
    if r%2 == 0:
        return power(n*n % mod, r//2, mod) % mod
    if r%2 == 1:
        return n * power(n, r-1, mod) % mod


def comb(n, k, mod=10**9+7):
    a=framod(n, mod)
    b=framod(k, mod)
    c=framod(n-k, mod)
    return (a * power(b, mod-2, mod) * power(c, mod-2, mod)) % mod


N, K = map(int, input().split())
R = N - K
mod = 10**9 + 7

ans = [0]*K
if R == 0:
  ans[0] = 1
elif R == 1:
  ans[0] = 2
  if K >= 2:
    ans[1] = (K-1) % mod
elif R == 2:
  ans[0] = 3
  if K >= 2:
    ans[1] = (3*K - 3) % mod
    if K >= 3:
      ans[2] = (K-1)*(K-2)//2 % mod
else:
  ans[0] = R + 1
  if K >= 2:
    if R > K:
      for i in range(2, K+1):
        ans[i-1] = comb(K-1, i-1)*(comb(R-1, i-2)+2*comb(R-1, i-1)+comb(R-1, i)) % mod
    else:
      for i in range(2, R):
        ans[i-1] = comb(K-1, i-1)*(comb(R-1, i-2)+2*comb(R-1, i-1)+comb(R-1, i)) % mod
      
      ans[R-1] = comb(K-1, R-1)*(comb(R-1, R-2)+2*comb(R-1, R-1)) % mod
      if R <= K-1:
        ans[R] = comb(K-1, R)*comb(R-1, R-1) % mod

for a in ans:
  print(a)