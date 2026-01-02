x,y,z,q=map(int,input().split())
a=sorted(map(int,input().split()),reverse=True)
b=sorted(map(int,input().split()),reverse=True)
c=sorted(map(int,input().split()),reverse=True)
 
def bisect(l,r):
  cnt=(l+r)//2
  if cnt==l:
    return l-1+judge(l)
  if judge(cnt):
    return bisect(cnt+1,r)
  else:
    return bisect(l,cnt)
def judge(thr):
  m=0
  for i in range(x):
    for j in range(y):
      if i*j>q:
        break
      for k in range(z):
        if i*j*k>q or a[i]+b[j]+c[k]<thr:
          break
        m+=1
        if m>=q:
          return True
  return False
def make(thr):
  m=0
  l=[]
  for i in a:
    for j in b:
      for k in c:
        n=i+j+k
        if n<thr+1:
          break
        m+=1
        l+=[n]
  l.sort(reverse=True)
  return l+[thr]*(q-len(l))
thr=bisect(0,a[0]+b[0]+c[0]+1)
ans=make(thr)
for w in ans:
  print(w)