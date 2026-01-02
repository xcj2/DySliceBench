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
  n=I()
  l=LI()

  ans=[]
  while True:
    if len(l)==0:
      break
    i=len(l)-1
    f=True
    for _ in range(len(l)):
      if l[i]==i+1:
        ans.append(l[i])
        l=l[:i]+l[i+1:]
        f=False
        break
      i-=1
    if f:
      print(-1)
      exit()
  ans.reverse()
  for x in ans:
    print(x)

main()
# print(main())
