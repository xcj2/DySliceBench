import math,itertools,fractions,heapq,collections,bisect,sys,queue,copy

sys.setrecursionlimit(10**7)
inf=10**20
mod=1000000007
dd=[(-1,0),(0,1),(1,0),(0,-1)]
ddn=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return input()

def main():
  n=I()

  s1=S()
  s2=S()

  i=0
  ans=1
  free=3
  while True:
    if i+1>n:
      return ans%mod

    if i==0:
      if s1[i]==s2[i]:
        ans*=3
        ans%=mod
        i+=1
        free=0
      else:
        ans*=6
        ans%=mod
        i+=2
        free=1
      continue

    if s1[i]==s2[i]:
      if free==0:
        ans*=2
        ans%=mod
      i+=1
      free=0
    else:
      if free==0:
        ans*=2
        ans%=mod
      else:
        ans*=3
        ans%=mod
      i+=2
      free=1

# main()
print(main())
