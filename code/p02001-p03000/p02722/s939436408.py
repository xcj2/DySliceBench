def MI():return map(int,input().split())
def LI():return list(MI())

def factorization(n):
  arr=[]
  temp=n
  for i in range(2,int(n**0.5)+1):
    if temp%i==0:
      cnt=0
      while temp%i==0:
        cnt+=1
        temp//=i
      arr.append([i,cnt])      
  if temp!=1:arr.append([temp,1])
  if arr==[]:arr.append([n,1])
  return arr

def make_divisors(n):
  divisors=[]
  for i in range(1,int(n**0.5)+1):
    if n%i==0:
      divisors.append(i)
      if i!=n//i:
        divisors.append(n//i)
  divisors.sort()
  return divisors[1:]

n=int(input())

l=[]
for k in make_divisors(n):
  NN=int(n)
  while NN>=k:
    if NN%k==0:
      NN=NN//k
    else:
      NN=NN%k
  if NN==1:l+=k,

ll=(l+make_divisors(n-1))

print(len(ll))
