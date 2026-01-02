L,A,B,mod=map(int,input().split())
def f(l):
  return max(0,(10**l-A-1)//B+1)

def m(a,b):
  r=[[0]*len(b[0]) for i in range(len(a))]
  for i in range(len(a)):
    for k in range(len(b)):
      for j in range(len(b[0])):
        r[i][j]=(r[i][j]+a[i][k]*b[k][j])%mod
  return r

def p(a,n):
  r=[[0]*len(a) for i in range(len(a))]
  b=[]
  for i in range(len(a)):
    r[i][i]=1
    b.append(a[i][:])
  l=n
  while l>0:
    if l&1:
      r=m(b,r)
    b=m(b,b)
    l>>=1
  return r

'''
100   001
B10 * 00s
01l   00P
'''

X=[[0,0,1],[0,0,A],[0,0,0]]
Y,R,Z=0,1,0
while L:
  Y=[[1,0,0],[B,1,0],[0,1,pow(10,R,mod)]]
  Z=min(L,f(R)-f(R-1))
  L-=Z
  Y=p(Y,Z)
  X=m(Y,X)
  R+=1
print(X[2][2]%mod)