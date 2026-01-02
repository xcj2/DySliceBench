n=int(input())
k=int(input())
d=len(str(n))
from math import factorial as f
def c(n):
  if n<2:
    return 0
  else:
    return f(n)//(f(n-2)*f(2))
def kk(n):
  dd=len(str(n))
  s=9*(dd-1)
  s+=int(str(n)[0])
  return s
def kkk(n):
  d=len(str(n))
  s=81*(d-1)*(d-2)//2
  s+=9*(d-1)*(int(str(n)[0])-1)
  s+=kk(int(str(n)[1:]))
  return s

if d==1 and k!=1:
  print(0)
else:
  if k==1:
    ans=kk(n)
  elif k==2:
    ans=kkk(n)
  else:
    t=0
    for i in range(2,d-1):
      t+=c(i)
    ans=729*t
    ans+=81*c(d-1)*(int(str(n)[0])-1)
    ans+=kkk(int(str(n)[1:]))
  print(ans)