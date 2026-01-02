n, m=map(int, input().split())
a=list(map(int, input().split()))
a.sort()
aa=a[:]
for i in range(n-2, -1, -1):
  aa[i]+=aa[i+1]

g=[0]*(a[-1]+1)
for i in range(n):
  g[a[i]]+=1
for i in range(a[-1]-1, -1, -1):
  g[i]+=g[i+1]
  
def f(index, point):
  tmp=point-a[index]
  if tmp>a[-1]:
    return 0
  elif tmp<=0:
    return n
  else:
    return g[tmp]
  
def ff(point):
  return sum([f(i, point) for i in range(n)])

def fff():
  x=0
  y=2*a[-1]+1
  c=(x+y)//2
  while y-x>1:
    if ff(c)>m:
      x=(x+y)//2
    else:
      y=(x+y)//2
    c=(x+y)//2
  return y

def ffff(index, point):
  tmp=f(index, point)
  if tmp>0:
    return aa[-tmp]+a[index]*tmp
  else:
    return 0
  
p=fff()
q=m-ff(p)
out=0
for i in range(n):
  out+=ffff(i, p)
out+=(p-1)*q
print(out)