N=int(input())

def cf(n):
  a=[]
  for f in range(1,int(n**(1/2)+1)):
    if n%f==0:
      a.append(f)
      if n//f!=f:
        a.append(n//f)
  return a

def pf(n):
  a=[]
  while n%2==0:
    a.append(2)
    n//=2
  f=3
  while f*f<=n:
    if n%f==0:
      a.append(f)
      n//=f
    else:
      f+=2
  if n!=1:
    a.append(n)
  return sorted(a)

def main():
  c,p,t=1,N+1,1
  for f in pf(N-1):
    if p==f:
      t+=1
    else:
      c*=t
      t=2
    p=f
  c=c*t-1

  for f in cf(N):
    t=N
    if f!=1:
      while t%f==0:
        t//=f
      if t%f==1:
        c+=1
  print(c)

main()
