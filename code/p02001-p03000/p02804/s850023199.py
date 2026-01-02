fact = [1]
p = 10**9 + 7

def fact1(n,m):
    for i in range(1,n+m+1):
        new_fact = fact[i-1]*i %p
        fact.append(new_fact)
#ax+by=1の解
def extgcd(a,b):
    r = [1,0,a]
    w = [0,1,b]
    while w[2] != 1:
        q = r[2]//w[2]
        r2 = w
        w2 = [r[0]-q*w[0],r[1]-q*w[1],r[2]-q*w[2]]
        r = r2
        w = w2
    return [w[0],w[1]]    
#aの逆元(mod m) a,mは互いに素
def mod_inv(a,m):
    x = extgcd(a,m)[0]
    return x%m

if __name__ == "__main__":
  n,k = (int(i) for i in input().split())
  a0 = [int(i) for i in input().split()]
  a = sorted(a0)
  fact1(n,0)
  minx = 0
  maxx = 0
  ck = mod_inv(fact[k-1],p)
  nck = [0]*k
  nck[k-1] = 1
  for i in range(k,n):
    tmp = mod_inv(fact[i-k+1],p)
    tmp2 = fact[i]*(ck*tmp%p)%p
    nck.append(tmp2)
  for i in range(1,n-k+2):
    minx = (minx + nck[n-i]*a[i-1])%p
    maxx = (maxx + nck[n-i]*a[n-i])%p
  ans = maxx - minx
  if ans < 0:
    ans += p
  print(ans)
   