x,y = map(int,input().split())
MOD = 10**9 + 7

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
  
#まず目的地まで行けるかどうか判定する。
#移動回数
n = (x+y)//3

a = -1
for i in range(n+1):
  if i+2*(n-i) == x and  2*i+(n-i) == y:
    a = i
    
if a == -1:
  print(0)
else:
  ans = comb(n,a,MOD)
  print(ans%MOD)
  