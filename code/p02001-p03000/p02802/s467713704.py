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
  n,k=LI()
  l=[False for _ in range(n)]
  l2=[0 for _ in range(n)]

  ans1=ans2=0
  for _ in range(k):
    a,b=LS()
    a=int(a)

    if b=='WA':
      if l[a-1]==False:
        l2[a-1]+=1
    else:
      if l[a-1]==False:
        l[a-1]=True
        ans1+=1
        ans2+=l2[a-1]

  return str(ans1)+' '+str(ans2)

# main()
print(main())
