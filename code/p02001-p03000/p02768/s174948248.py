import math,itertools,fractions,heapq,collections,bisect,sys,queue,copy

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7
dd=[(-1,0),(0,1),(1,0),(0,-1)]
ddn=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return input()

def cmb(n, r, p):
  a=1
  for i in range(r):
    a*=n
    a%=mod
    n-=1
  b=1
  for i in range(1,r+1):
    b*=i
    b%=mod

  inv_b=mod_inv(b,mod)
  # print(a,inv_b)
  return a*inv_b

def pow_k(x, n):
    """
    O(log n)
    """
    if n == 0:
        return 1

    K = 1
    while n > 1:
        if n % 2 != 0:
            K *= x
            K%=mod
        x *= x
        n //= 2
        x%=mod

    return (K * x)%mod

def extgcd(a,b):
    r = [1,0,a]
    w = [0,1,b]
    while w[2]!=1:
        q = r[2]//w[2]
        r2 = w
        w2 = [r[0]-q*w[0],r[1]-q*w[1],r[2]-q*w[2]]
        r = r2
        w = w2
    #[x,y]
    return [w[0],w[1]]

def mod_inv(a,m):
    x = extgcd(a,m)[0]
    return (m+x%m)%m

def main():
  n,a,b=LI()
  if n==2:
    if a!=b:
      return 0
    else:
      return 1

  ans=pow_k(2,n)

  ans-=(cmb(n,a,mod)%mod)
  ans-=(cmb(n,b,mod)%mod)

  ans-=1
  ans%=mod

  if ans<0:
    ans+=mod

  return ans

# main()
print(main())
