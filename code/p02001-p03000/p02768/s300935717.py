def mpow(a,n,mod):
  if n == 0:
    return 1
  elif n == 1:
    return a
  elif n%2==0:
    return (pow(a,n//2,mod))**2%mod
  else:
    return a*pow(a,n-1,mod)%mod
def mfac(l,r,mod):
  ans = l
  for i in reversed(range(r,l)):
    ans *= i
    ans %= mod
  return ans
def mcomb(n,k,mod):
  A = mfac(n,n-k+1,mod)
  B = mfac(k,1,mod)
  B = mpow(B,mod-2,mod)
  return A*B%mod

def main():
  mod = 10**9+7
  n,a,b = map(int,input().split(" "))
  ans = mpow(2,n,mod)-1-mcomb(n,a,mod)-mcomb(n,b,mod)
  ans %= mod
  print(ans)

if __name__ == "__main__":
  main()