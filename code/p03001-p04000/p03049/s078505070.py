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
  ans=0

  _ba=0
  _b=0
  _a=0
  for _ in range(n):
    s=S()
    ans+=s.count('AB')

    if s[0]=='B':
      if s[-1]=='A':
        _ba+=1
      else:
        _b+=1
    else:
      if s[-1]=='A':
        _a+=1

  ans+=max(0,_ba-1)

  if _ba>0:
    if _b>0:
      ans+=1
      _b-=1
    if _a>0:
      ans+=1
      _a-=1

  # if _ba>0:
  #   _b+=1
  #   _a+=1

  ans+=min(_b,_a)

  return ans

# main()
print(main())
