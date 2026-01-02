n=int(input())
s=list(input())
q=int(input())
c=[chr(i) for i in range(97, 97+26)]
l=[input().split() for i in range(q)]

def segfunc(x,y):
  return x+y

def init(init_val,c):
  for i in range(n):
    seg[c][i+num-1]=init_val[i]
  for i in range(num-2,-1,-1):
    seg[c][i]=segfunc(seg[c][2*i+1],seg[c][2*i+2])

def update(k,x,c):
  k+=num-1
  seg[c][k]+=x
  while k:
    k=(k-1)//2
    seg[c][k]=segfunc(seg[c][k*2+1],seg[c][k*2+2])

def query(p,q,c):
  if q<=p:
    return ide_ele
  p+=num-1
  q+=num-2
  res=ide_ele
  while q-p>1:
    if p&1==0:
      res=segfunc(res,seg[c][p])
    if q&1==1:
      res=segfunc(res,seg[c][q])
      q-=1
    p=p//2
    q=(q-1)//2
  if p==q:
    res=segfunc(res,seg[c][p])
  else:
    res=segfunc(segfunc(res,seg[c][p]),seg[c][q])
  return res

ide_ele=0

num=2**(n-1).bit_length()
seg=[[ide_ele]*2*num for i in range(26)]

L=[[0 for i in range(n)] for j in range(26)]
for i in range(n):
  L[c.index(s[i])][i]+=1

for i in range(26):
  init(L[i],i)

for i in range(q):
  if l[i][0]=='1':
    update(int(l[i][1])-1,1,c.index(l[i][2]))
    update(int(l[i][1])-1,-1,c.index(s[int(l[i][1])-1]))
    s[int(l[i][1])-1]=l[i][2]
  else:
    ct=0
    for j in range(26):
      if query(int(l[i][1])-1,int(l[i][2]),j)!=0:
        ct+=1
    print(ct)