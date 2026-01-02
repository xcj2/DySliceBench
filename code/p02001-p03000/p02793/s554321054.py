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

def primes(n):
  is_prime=[True]*(n+1)
  is_prime[0]=False
  is_prime[1]=False
  for i in range(2,int(n**0.5)+1):
    if not is_prime[i]:
      continue
    for j in range(i*2,n+1,i):
      is_prime[j]=False
  return [i for i in range(n+1) if is_prime[i]]

prime=primes(int(10**3)+1)

def fact2(n):
  l=prime
  L=[]
  for i in range(len(l)):
    ct=0
    while n%l[i]==0:
      n=n//l[i]
      ct+=1
    if ct!=0:
      L.append((l[i],ct))
    if n==1:
      break
  if n!=1:
    L.append((n,1))
  return L

n=int(input())
a=list(map(int,input().split()))
l=[0 for i in range(10**6)]
mod=10**9+7
for i in range(n):
  x=fact2(a[i])
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