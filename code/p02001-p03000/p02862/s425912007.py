MOD=1000000007

def combination(n,m):
    if m==0:
        return 1
    else:
        return combination(n-1,m-1)*n//m

def pow_mod(a, b, p):
    if b == 0:
        return 1
    elif b%2 == 0:
        d = pow_mod(a, b//2, p)
        return (d**2)%p
    else:
        return (a*pow_mod(a,b-1,p))%p    
    
def factorial_mod(n,p):
    tmp = 1
    for i in range(1,n+1):
        tmp *= i
        tmp %= p
    return tmp


      
x,y=map(int,input().split())
if (x+y)%3!=0:
  print(0)
elif x*2<y:
  print(0)
elif y*2<x:
  print(0)
else:
  a=(x+y)//3
  x-=a
  y-=a
  #x+yCx
  if x>y:
    a=x
    x=y
    y=a
  W=x+1
  H=y+1
  ans = factorial_mod(W-1 + H-1, MOD)
  ans *= pow_mod(factorial_mod(H-1,MOD), MOD-2, MOD)
  ans %= MOD
  ans *= pow_mod(factorial_mod(W-1,MOD), MOD-2, MOD)
  ans %= MOD

 
  print(ans)
  
 