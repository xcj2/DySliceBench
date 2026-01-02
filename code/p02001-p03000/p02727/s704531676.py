import math,itertools,fractions,heapq,collections,bisect,sys,queue,copy

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7
dd=[(-1,0),(0,1),(1,0),(0,-1)]
ddn=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return input()

def main():
  x,y,a,b,c=LI()
  la=LI()
  lb=LI()
  lc=LI()

  la.sort(reverse=True)
  lb.sort(reverse=True)
  lc.sort(reverse=True)

  ans_list=[]
  ans_list+=la[:x]
  ans_list+=lb[:y]
  ans_list+=lc[:(x+y)]

  ans_list.sort(reverse=True)


  # print(ans_list)
  return sum(ans_list[:x+y])

# main()
print(main())
