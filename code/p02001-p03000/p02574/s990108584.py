n=int(input())
a=list(map(int,input().split()))

def gcd(a,b):
  if b==0:
    return a
  else:
    return gcd(b,a%b)

#高速素因数分解

#エラストテネスのふるい
#sieveが0なら素数、0以外ならその値を割り切る素数
def create_sieve(n):
  sieve=[0]*(n+1)
  for i in range(2,n+1):
    if sieve[i]==0:
      for j in range(i*i,n+1,i):
        sieve[j]=i
  return sieve
#素因数分解
#dicではkey=素数、value=何乗か
def prime(n,sieve):
  dic={}
  while(1):
    if sieve[n]==0:
      dic[n]=dic.get(n,0)+1
      break
    else:
      p=sieve[n]
      dic[p]=dic.get(p,0)+1
      n=n//p
  return dic

def setwise(a):
  l=a[0]
  for i in range(len(a)):
    l=gcd(l,a[i])
  return l==1


if setwise(a):
  check=set()
  sieve=create_sieve(max(a))
  for num in a:
    if num!=1:
      dic=prime(num,sieve)
      for j in dic:
        if j in check:
          print("setwise coprime")
          exit()
        else:
          check.add(j)
  print("pairwise coprime")
  
else:
  print("not coprime")
  
  
  