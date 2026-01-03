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
  a=inf
  b=0
  ans1=[]
  ans2=[]

  N,T=LI()
  l=LI()

  a=l[0]
  for x in l[1:]:
    if x<a:
      ans1.append([a,b])
      ans2.append(b-a)
      a=x
      b=x
    else:
      b=max(b,x)
  ans1.append([a,b])
  ans2.append(b-a)

  ans2.sort()
  return ans2.count(ans2[-1])

# main()
print(main())
