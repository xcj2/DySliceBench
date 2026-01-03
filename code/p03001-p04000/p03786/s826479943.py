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

  l.sort()
  for i in range(n-1):
    l[i+1]+=l[i]

  # print(l)
  
  ans=n
  c=1
  for i in range(n-1):
    if l[i+1]-l[i]>l[i]*2:
      ans-=c
      c=1
    else:
      c+=1

  return ans

# main()
print(main())
