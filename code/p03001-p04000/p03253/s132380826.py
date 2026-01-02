def pmod(a,b,m):
  ret=1
  while b>0:
    if b&1:
      ret=(ret*a)%m
    a=(a*a)%m
    b=b>>1
  return ret
  
def fmod(n,m):
  ret=1
  for i in range(n,0,-1):
    ret=(ret*i)%m
  return ret

def cmod(n,r,m):
  ret=1
  for i in range(r):
    ret=(ret*(n-i))%m
  return (ret*pmod(fmod(r,m),m-2,m))%m

def div(num):
  ret=[]
  for i in range(2,int(num**0.5)+1):
    if num%i==0:
      ret.append(i)
      num=num//i
      while num%i==0:
        ret.append(i)
        num=num//i
  if num!=1:
    ret.append(num)
  return ret

n,m=map(int,input().split())
MOD=10**9+7
d=div(m)
dic={}
for i in d:
  if i not in dic:
    dic[i]=1
  else:
    dic[i]+=1
ans=1
for i in dic.values():
  ans=(ans*cmod(n-1+i,n-1,MOD))%MOD
print(ans)