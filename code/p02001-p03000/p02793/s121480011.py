def extgcd(a,b):
  r=[1,0,a]
  w=[0,1,b]
  while w[2]!=1:
    q=r[2]//w[2]
    r2=w
    w2=[r[0]-q*w[0],r[1]-q*w[1],r[2]-q*w[2]]
    r=r2
    w=w2
  return [w[0],w[1]]
def mod_inv(a,m):
  x=extgcd(a,m)[0]
  return (m+x%m)%m

def fact(n):
  fct=[]
  b,e=2,0
  while b*b<= n:
    while n%b==0:
      n=n//b
      e=e + 1
    if e>0:
      fct.append((b, e))
    b,e=b+1,0
  if n>1:
    fct.append((n, 1))
  return fct

n=int(input())
a=list(map(int,input().split()))
l=[0 for i in range(10**6)]
mod=10**9+7
for i in range(n):
  x=fact(a[i])
  for j in range(len(x)):
    l[x[j][0]]=max(l[x[j][0]],x[j][1])
lcm=1
for i in range(2,10**6):
  lcm*=(i**l[i])
  lcm%=mod
ans=0
for i in range(n):
  ans+=lcm*mod_inv(a[i],mod)
  ans%=mod
print(ans)