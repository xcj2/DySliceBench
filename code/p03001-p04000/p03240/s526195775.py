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
  l=[LI() for _ in range(n)]

  l=sorted(l,key=lambda x:x[2],reverse=True)

  ans=[]
  for Cx in range(101):
    for Cy in range(101):
      H=l[0][2]+abs(l[0][0]-Cx)+abs(l[0][1]-Cy)
      f=True
      for x,y,h in l[1:]:
        if h!=max(H-abs(x-Cx)-abs(y-Cy),0):
          f=False
          break
      if f:
        ans.append(str(Cx)+' '+str(Cy)+' '+str(H))
  if len(ans)==1:
    return ans[0]

# main()
print(main())
