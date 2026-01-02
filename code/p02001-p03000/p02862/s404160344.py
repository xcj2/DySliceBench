def sq(a, b, mod):  # aのb乗を剰余
    if b == 0:
        return 1
    elif b % 2 == 0:
        return sq(a, b // 2, mod)**2 % mod
    else:
        return sq(a, b - 1, mod) * a % mod
  
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def nCk(n,k,mod):
  prev=1
  for i in range(1,min(k,n-k)+1):
    v=(prev * (n+1-i) % mod * modinv(i, mod) % mod)
    prev=v
  return prev

x,y=map(int,input().split())
mod=10**9+7

if (x+y)%3!=0:
  print(0)
else:
  n=(x+y)//3
  k=(2*x-y)//3
  if k<0 or k>n:
    print(0)
  else:
    print(nCk(n,k,mod))