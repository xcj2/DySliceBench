import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,queue,copy

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7
dd=[(-1,0),(0,1),(1,0),(0,-1)]
ddn=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return input()

# Factoring by trial split
def getPrimeList(n):
  l=[]
  t=int(math.sqrt(n))+1
  
  for a in range(2,t):
    while n%a==0:
      n//=a
      l.append(a)
  
  if n!=1:
    l.append(n)
  
  return l

def main():
  a,b=LI()

  if a==1 and b==1:
    return 1

  a=getPrimeList(a)
  b=getPrimeList(b)

  a=list(set(a))
  b=list(set(b))

  c=a+b
  c.sort()

  ans=1
  y=c[0]
  cnt=1
  for x in c[1:]:
    if x==y:
      cnt+=1
    else:
      y=x
      cnt=1

    if cnt==2:
      ans+=1

  return ans

# main()
print(main())
