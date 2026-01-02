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
  n=I()
  l1=LI()
  l2=LI()

  sm1=sum(l1)
  sm2=sum(l2)

  nm=sm2-sm1
  if nm<0:
    return 'No'

  nm1=0
  for i in range(n):
    a=l1[i]
    b=l2[i]

    if a<b:
      _a=(b-a+1)//2
      l1[i]+=_a*2
      nm1+=_a

  nm2=0
  for i in range(n):
    a=l1[i]
    b=l2[i]

    if a>b:
      _a=a-b
      nm2+=_a

  # print(nm,nm2)
  if nm<max(nm1,nm2):
    return 'No'

  return 'Yes'

# main()
print(main())
