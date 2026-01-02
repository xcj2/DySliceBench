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
  a,b,c,d,e,f=LI()

  ans_n=-inf
  ans_pair=[0,0]
  xf=100*e/(100+e)
  for i in range(31):
    for j in range(31):
      for k in range(101):
        for l in range(101):
          xa=100*a*i+100*b*j
          xb=c*k+d*l

          # print(xa,xb)
          if xa+xb>f:
            break

          if xa+xb==0:
            continue

          xc=100*xb/(xa+xb)
          if xc>xf:
            continue

          if ans_n<xc:
            ans_n=xc
            ans_pair=[xa+xb,xb]

  return str(ans_pair[0])+' '+str(ans_pair[1])

# main()
print(main())
