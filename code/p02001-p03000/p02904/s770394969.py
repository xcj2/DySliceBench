def main():
  def update(k,x):
    k+=N0-1
    data_min[k]=data_max[k]=x
    while k>=0:
      k=(k-1)//2
      a,b=data_min[2*k+1],data_min[2*k+2]
      data_min[k]=a if a<b else b
      a,b=data_max[2*k+1],data_max[2*k+2]
      data_max[k]=a if a>b else b
  def query_min(l,r):
    L,R=l+N0,r+N0
    s=INF
    while L<R:
      if R&1:
        R-=1
        t=data_min[R-1]
        if t<s:s=t
      if L&1:
        t=data_min[L-1]
        if t<s:s=t
        L+=1
      L//=2
      R//=2
    return s
  def query_max(l,r):
    L,R=l+N0,r+N0
    s=0
    while L<R:
      if R&1:
        R-=1
        t=data_max[R-1]
        if t>s:s=t
      if L&1:
        t=data_max[L-1]
        if t>s:s=t
        L+=1
      L//=2
      R//=2
    return s
  n,k,*p=map(int,open(0).read().split())
  N0=2**(n-1).bit_length()
  INF=10**18
  data_min=[INF]*2*N0
  data_max=[0]*2*N0
  c=[0]
  for a,b in zip(p,p[1:]):c+=c[-1]+(a<b),
  *c,f=[b-a==k-1for a,b in zip(c,c[k-1:])]
  x=not f
  for i,q in enumerate(p):update(i,q)
  for i,(a,b,c)in enumerate(zip(p,p[k:],c)):
    f|=c
    if not c and(a!=query_min(i,i+k)or b!=query_max(i+1,i+k+1)):x+=1
  print(x+f)
main()