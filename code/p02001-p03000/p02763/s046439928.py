def i1():
 return int(input())
def i2():
 return [int(i) for i in input().split()]
import sys
sys.setrecursionlimit(10**6)

n=i1()
s=input()
q=i1()
N=0
while n:
  n>>=1
  N+=1
n=2**N

t=[0 for i in range(2*n-1)]

def ud(i,x):
  i+=n-1
  t[i]=x
  while i:
    i=(i-1)//2
    t[i]=t[i*2+1] | t[i*2+2]

def qr(a,b,k,l,r):
  
  if r<=a or b<=l:
     return 0
  elif a<=l and r<=b:
     
     return t[k]
  else:
     return qr(a,b,k*2+1,l,(l+r)//2) | qr(a,b,k*2+2,(l+r)//2,r)

for i in range(len(s)):
  ud(i,1<<(ord(s[i])-ord("a")))

while q:
 [ty,i,c]=[i for i in input().split()]
 ty=int(ty)
 i=int(i)
 if ty==1:
   ud(i-1,1<<(ord(c)-ord("a")))
 else:
   c=int(c)
   x=0
   z=qr(i-1,c,0,0,n)
   while z:
     if z%2==1:
        x+=1
     z>>=1
   print(x)
 q-=1
