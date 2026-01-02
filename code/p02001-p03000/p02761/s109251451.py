import math,itertools,fractions,heapq,collections,bisect,sys,queue,copy

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7
dd=[(-1,0),(0,1),(1,0),(0,-1)]
ddn=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return input()

def main():
  n,m=LI()
  ans=[-1]*n

  f=False
  for i in range(m):
    a,b=LI()
    a-=1
    if ans[a]!=-1:
      if ans[a]!=b:
        f=True
    else:
      ans[a]=b

  if f:
    return -1

  _ans=''
  for i,x in enumerate(ans):
    if x==-1:
      if i==0 and n!=1:
        _ans+='1'
      else:
        _ans+='0'
    else:
      _ans+=str(x)

  __ans=int(_ans)
  if len(str(__ans))<n:
    return -1

  return _ans

# main()
print(main())
