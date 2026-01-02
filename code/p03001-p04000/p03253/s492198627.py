import collections
def cmb(n,r,mod):
  if r<0 or r>n:
    return 0
  r=min(r,n-r)
  return g1[n]*g2[r]*g2[n-r]%mod

n,M=map(int,input().split())
m=10**9+7
 
g1=[1,1]
g2=[1,1]
inverse=[0,1]
 
for i in range(2,n+100):
  g1.append((g1[-1]*i)%m)
  inverse.append((-inverse[m%i]*(m//i))%m)
  g2.append((g2[-1]*inverse[-1])%m)

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

def fact(n):
  l=primes(int(n**0.5)+1)
  L=[]
  for i in range(len(l)):
    while n%l[i]==0:
      n=n//l[i]
      L.append(l[i])
    if n==1:
      break
  if n!=1:
    L.append(n)
  return L

x=list(collections.Counter(fact(M)).values())
ct=1
for i in range(len(x)):
  ct*=cmb(x[i]+n-1,n-1,m)
  ct%=m
print(ct)