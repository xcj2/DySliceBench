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
  N=I()
  s=S()

  l=[0]*10
  for x in s:
    i=int(x)
    l[i]+=1
  check0=[0]*10

  ans=0
  for i,x in enumerate(s):
    _x=int(x)
    l[_x]-=1

    if check0[_x]!=0:
      continue

    check0[_x]=1

    check=[0]*10
    l2=copy.deepcopy(l)
    for y in s[i+1:]:
      _y=int(y)
      l2[_y]-=1
      if check[_y]!=0:
        continue

      check[_y]=1

      for x in l2:
        if x!=0:
          ans+=1

  return ans

# main()
print(main())
