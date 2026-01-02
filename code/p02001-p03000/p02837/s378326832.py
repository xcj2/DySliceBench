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
  l=[]
  for i in range(1<<n):
    _l=[]
    for j in range(n):
      _l.append(1 if i&(1<<j) else 0)
    l.append(_l)

  l2=[]
  for _ in range(n):
    a=I()
    _l2=[]
    for __ in range(a):
      _l2.append(LI())
    l2.append(_l2)

  ans=0
  for x in l:
    f=True
    for i,y in enumerate(x):
      if y==1:
        for z1,z2 in l2[i]:
          if x[z1-1]!=z2:
            f=False
            break
        if not f:
          break
    if f:
      ans=max(ans,x.count(1))

  return ans

# main()
print(main())
