import math,itertools,fractions,heapq,collections,bisect,sys,queue,copy

sys.setrecursionlimit(10**7)
inf=10**20
mod=998244353
dd=[(-1,0),(0,1),(1,0),(0,-1)]
ddn=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return input()

def main():
  n,p=LI()
  s=S()

  ans=0
  if p==2 or p==5:
    for i,x in enumerate(s):
      if int(x)%p==0:
        ans+=i+1
    return ans

  _s=list(s)
  _s.reverse()

  a=[]
  i=1
  for x in _s:
    b=(i*int(x))%p
    a.append(b)
    i*=10
    i%=p

  b=[0]*p
  b[a[0]%p]=1
  for i in range(n-1):
    a[i+1]+=a[i]
    a[i+1]%=p
    b[a[i+1]]+=1

  for i,x in enumerate(b):
    if i==0:
      ans+=x
    if x>1:
      ans+=x*(x-1)//2

  return ans

# main()
print(main())
