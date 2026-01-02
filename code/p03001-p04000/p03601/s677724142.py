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

  z=100*e/(100+e)
  # print(z)
  
  for i in range(31):
    for j in range(31):
      for k in range(3001):
        for l in range(3001):
          _a=a*i*100+b*j*100
          _b=k*c+l*d

          if _a+_b>f:
            break

          if _a+_b==0:
            break

          y=100*_b/(_a+_b)

          if y<=z:
            if ans_n<=y:
              ans_n=y
              ans_pair=[_a+_b,_b]

  return str(ans_pair[0])+' '+str(ans_pair[1])

# main()
print(main())
