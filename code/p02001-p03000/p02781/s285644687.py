import sys
n=list(input())
N=len(n)
k=int(input())
x=int(n[0])
if N<k:
  print(0)
  sys.exit()

def s1(m):
  N=len(m)
  x=int(m[0])
  if N>1 and x==0:
    m2=m[1:N+1]
    return s1(m2)
  elif x==0:
    return 0
  else:
    ans=0
    ans+=(N-1)*9
    ans+=x
    return ans

def s2(m):
  N=len(m)
  x=int(m[0])
  if N>1 and x==0:
    m2=m[1:N+1]
    return s2(m2)
  elif x==0:
    return 0
  else:
    ans=0
    ans+=((N-1)*(N-2))*81//2
    ans+=((x-1)*(N-1))*9
    m2=m[1:N+1]
    ans+=s1(m2)
    return ans
  
def s3(m):
  N=len(m)
  x=int(m[0])
  if N>1 and x==0:
    m2=m[1:N+1]
    return s3(m2)
  elif x==0:
    return 0
  else:
    ans=0
    ans+=((N-1)*(N-2)*(N-3)*729)//6
    ans+=((x-1)*(N-1)*(N-2)*81)//2
    m2=m[1:N+1]
    ans+=s2(m2)
    return ans

if k==1:
  print(s1(n))
  sys.exit()

if k==2:
  print(s2(n))
  sys.exit()

if k==3:
  print(s3(n))
  sys.exit()