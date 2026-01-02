n,a,b=map(int,input().split())

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
      
mod=10**9+7    
tot=sq(2,n,mod)
prev=1
for i in range(1,min(n+1,2*10**5+1)):
  v=(prev * (n+1-i) % mod * modinv(i, mod) % mod)
  prev=v
  if i==a or i==b:
    tot-=v
    
print((tot-1)%mod)