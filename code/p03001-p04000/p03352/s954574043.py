def factorize(m):
  facs=[]
  i=2
  if m==1:
    return [0]
  while m>1:
    j=0
    if m%i!=0:
      i+=1
    while m%i==0:
      j+=1
      m/=i
      if m%i!=0:
        facs.append(j)
        i+=1
        break
  return facs

def GCM(m,n):
  if m>n:
    m,n=n,m
  gcm=m
  while gcm>1:
    if n%gcm==0 and m%gcm==0:
      return gcm
    else:
      gcm-=1
  return 1

def GCM_many(s):
  gcm=s[0]
  for i in range(1,len(s)):
    gcm=GCM(gcm,s[i])
  return gcm

n=int(input())
if n==1:
  print(1)
  exit()
for i in range(1, n+1)[::-1]:
  facs=factorize(i)
  if GCM_many(facs)>1:
    print(i)
    exit()
print(1)