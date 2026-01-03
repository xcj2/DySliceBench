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
  n=I()
  l=getPrimeList(n)

  mn=len(str(n))
  for i in range(2**len(l)):
    a=n
    b=1
    for j in range(len(l)):
      if ((i>>j)&1):
        a//=l[j]
        b*=l[j]
    mn=min(mn,max(len(str(a)),len(str(b))))

  return mn

# main()
print(main())
