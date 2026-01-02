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
  s=S()
  n=len(s)
  ls=list(s)

  f=True
  _s=copy.deepcopy(ls)
  _s.reverse()
  if _s!=ls:
    f=False

  ls2=ls[:(n-1)//2]
  _ls2=copy.deepcopy(ls2)
  _ls2.reverse()

  if ls2!=_ls2:
    f=False

  ls3=ls[(n+3)//2-1:]
  _ls3=copy.deepcopy(ls3)
  _ls3.reverse()

  if ls3!=_ls3:
    f=False

  # print(ls,_s)
  # print(ls2,_ls2)
  # print(ls3,_ls3)

  if f:
    return 'Yes'
  return 'No'

# main()
print(main())
