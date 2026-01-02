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
  a,b,c,d,e,f=LI()
  ans=-inf
  ans_pair=[]
  lim=(100*e)/(100+e)
  for i in range(31):
    for j in range(31):
      for k in range(f//c+1):
        for l in range(f//d+1):
          mi=100*a*i+100*b*j
          sa=c*k+d*l
          s=mi+sa

          if s==0:
            continue

          if s>f:
            break

          noudo=(100*sa)/s
          if noudo>lim:
            break

          if ans<=noudo:
            ans=noudo
            ans_pair=[s,sa]

  return str(ans_pair[0])+' '+str(ans_pair[1])

# main()
print(main())
