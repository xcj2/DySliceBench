import math,itertools,fractions,heapq,collections,bisect,sys,queue,copy

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7
dd=[(-1,0),(0,1),(1,0),(0,-1)]
ddn=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
# def LF(): return [float(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return input()

def main():
  N=I()
  A=LI()

  g=0
  for x in A:
    g=math.gcd(g,x)
  if g>1:
    return 'not coprime'

  sosu=[0]*1000100
  for x in A:
    if x==1:
      continue
    sosu[x]+=1
    if sosu[x]>1:
      return 'setwise coprime'
    for y in range(2,int(math.sqrt(x))+1):
      if x%y!=0:
        continue
      z=x//y
      if y==z:
        sosu[y]+=1
        if sosu[y]>1:
          return 'setwise coprime'
      else:
        sosu[y]+=1
        if sosu[y]>1:
          return 'setwise coprime'
        sosu[z]+=1
        if sosu[z]>1:
          return 'setwise coprime'

  return 'pairwise coprime'

# main()
print(main())
