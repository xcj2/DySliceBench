#互いに素なa,bについて、a*x+b*y=1の一つの解
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
  n,a,b=map(int,input().split())
  mod=10**9+7
  cmb_l=[1 for _ in range(b+1)]
  for i in range(b):
    cmb_l[i+1]=(cmb_l[i]*(n-i)%mod*mod_inv(i+1,mod))%mod

  x=cmb_l[a]
  y=cmb_l[b]
  return((2**n-x-y-1) % mod)
print(main())