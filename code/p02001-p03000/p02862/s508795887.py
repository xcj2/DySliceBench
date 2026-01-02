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

def cmb(n, r):
  if n - r < r: r = n - r
  if r == 0: return 1
  if r == 1: return n

  numerator = [n - r + k + 1 for k in range(r)]
  denominator = [k + 1 for k in range(r)]

  for p in range(2,r+1):
    pivot = denominator[p - 1]
    if pivot > 1:
      offset = (n - r) % p
      for k in range(p-1,r,p):
        numerator[k - offset] /= pivot
        denominator[k] /= pivot

  result = 1
  for k in range(r):
    if numerator[k] > 1:
      result *= int(numerator[k])

  return result

# nCr
def nCr(n,r):
  if n<r:
    return 0
  return math.factorial(n)//(math.factorial(n-r)*math.factorial(r))

def main():
  x,y=LI()

  if min(x,y)*2<max(x,y):
    return 0

  sm=x+y
  if sm%3!=0:
    return 0

  cnt=sm//3
  ac=cnt//2-((x-y)//2)
  bc=cnt-ac

  # print(ac)
  # print(bc)

  return cmb(cnt,ac)%mod


# main()
print(main())
