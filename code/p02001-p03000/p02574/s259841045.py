n=int(input())
a=list(map(int,input().split()))

import sys
import math
def setwise_coprime(a):
  ans=a[0]
  for i in range(1,n):
    ans=math.gcd(ans,a[i])
  return ans

#エラストテネスのふるい
def create_sieve(n):
  sieve=[0]*(n+1)
  for i in range(2,n+1):
    if sieve[i]==0:
      for j in range(i*i,n+1,i):
        sieve[j]=i
  return sieve

#高速素因数分解
def fast_factorization(n, sieve):
  prime={}
  while n>1:
    p=sieve[n]
    #nが素数の場合
    if p==0:
      prime[n]=prime.get(n,0)+1
      break
    #nが素数ではない場合
    else:
      prime[p]=prime.get(p,0)+1
      n=n//p
  return prime

check=set()
if setwise_coprime(a)==1:
  #素因数のダブリをcheck
  sieve=create_sieve(10**6)
  for i in range(n):
    if a[i]!=1:
      s=fast_factorization(a[i], sieve)
      for i in s:
        if i in check:
          print("setwise coprime")
          sys.exit()
        else:
          check.add(i)
  print("pairwise coprime")    
else:
  print("not coprime")
  
  



      
      
    
