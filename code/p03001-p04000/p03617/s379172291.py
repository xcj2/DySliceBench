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

def main():
  q,h,s,d=LI()
  n=I()

  q*=4
  h*=4
  s*=4
  d*=4
  n*=4

  l=[]
  l.append([q,1,q/1])
  l.append([h,2,h/2])
  l.append([s,4,s/4])
  l.append([d,8,d/8])

  l=sorted(l,key=lambda x:x[2])

  ans=0
  for x in l:
    if n%x[1]==0:
      ans+=(n//x[1])*x[0]
      return ans//4
    else:
      ans+=(n//x[1])*x[0]
      n%=x[1]

# main()
print(main())
