## 合計は2^NからnCaとnCbを引いたものに等しいので
n,a,b = list(map(int,input().split()))

mod = int(1e9+7)
ans = 1

def calc(n,mod):
  if n>25:
    return ( (calc(n//2,mod) **2 ) * (2 if n%2 == 1 else 1) )% mod
  else:
    return (2**n) % mod
    
ans = calc(n,mod)
  
def xgcd(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

def modinv(a, m):
    g, x, y = xgcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
  
a1 = 1
for i in range(1,a+1):
  a1 = int((a1*(n-a+i))*modinv(i,mod))%mod

b1 = 1
for i in range(1,b+1):
  b1 = int((b1*(n-b+i))*modinv(i,mod))%mod
  
print(int((ans-1-b1-a1))%mod)