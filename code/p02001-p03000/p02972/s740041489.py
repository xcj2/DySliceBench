import math,itertools,fractions,heapq,bisect,sys,queue,copy

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
  n=I()
  l=LI()

  ans=[0]*n

  ind=n
  for i in range(n):
    sm=0
    for j in range(2,n+1):
      if ind*j>n:
        break
      else:
        sm+=ans[ind*j-1]
    ans[ind-1]=(l[ind-1]+sm)%2
    ind-=1
    # print(ans,ind)

  # print(ans)

  _ans=[]
  for i,x in enumerate(ans):
    if x==1:
      _ans.append(i+1)

  ln=len(_ans)
  print(ln)
  if ln!=0:
    print(' '.join([str(x) for x in _ans]))

main()
# print(main())
