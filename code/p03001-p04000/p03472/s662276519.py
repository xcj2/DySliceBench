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
  n,h=LI()
  l=[]

  for _ in range(n):
    a,b=LI()
    l.append([a,-1])
    l.append([b,1])

  l=sorted(l,key=lambda x:x[0],reverse=True)
  # print(l)

  ans=0
  for i,x in enumerate(l):
    if x[1]==1:
      ans+=1
      h-=x[0]
    else:
      ans+=-(-h//x[0])
      return ans

    if h<=0:
      return ans

  return ans

# main()
print(main())
