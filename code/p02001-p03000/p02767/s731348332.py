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
  l=LI()

  l.sort()
  # center1=(l[0]+l[-1]+1)//2
  # center2=(l[0]+l[-1]-1)//2

  avg=sum(l)/len(l)
  center1=-(-avg//1)
  center2=int(avg)

  ans1=0
  ans2=0
  for x in l:
    ans1+=(x-center1)**2
    ans2+=(x-center2)**2

  # print(center1,center2,ans1,ans2)
  return int(min(ans1,ans2))

# main()
print(main())
