def framod(n, mod, a=1):
    for i in range(1,n+1):
        a=a * i % mod
    return a

def power(n, r, mod):
    if r == 0: return 1
    if r%2 == 0:
        return power(n*n % mod, r//2, mod) % mod
    if r%2 == 1:
        return n * power(n, r-1, mod) % mod

def comb(n, k, mod):
    a=framod(n, mod)
    b=framod(k, mod)
    c=framod(n-k, mod)
    return (a * power(b, mod-2, mod) * power(c, mod-2, mod)) % mod
  
X, Y = map(int,input().split())

mm = (2*Y - X) / 3
nn = (2*X - Y) / 3

ans = 0

if mm.is_integer() and nn.is_integer():
    mm = int(mm)
    nn = int(nn)
    if mm >=0 and nn>=0:
        ans =comb(mm+nn, nn, 10**9+7)
      
print(ans)
