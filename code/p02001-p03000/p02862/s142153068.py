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

# aの逆元(mod m)を求める。(aとmは互いに素であることが前提)
def mod_inv(a,m):
    if a%m!=0:
      x = extgcd(a,m)[0]
      return (m+x%m)%m
      

#nCk mod m を計算する(デフォルトの引数は10**9+7)
def c_mod(n,k,m=10**9+7):
  res = 1
  for i in range(1,n+1):
      if (i%m)!=0:
        res = res*i%m
      else:
        res=res/i%m
  for i in range(1,k+1):
      if (i%m)!=0:
        res = res*mod_inv(i,m)%m
      else:
        res=res/i%m
  for i in range(1,n-k+1):
      if (i%m)!=0:
        res = res*mod_inv(i,m)%m
      else:
        res=res/i%m
  return res


x,y=map(int,input().split())
if (2*x-y)%3==0 and (2*y-x)%3==0 and (2*y-x)>=0 and (2*x-y)>=0 :
  l=int((2*x-y)/3)
  k=int((2*y-x)/3)
  ans=c_mod(l+k,k)

else:
  ans=0
print(ans)
