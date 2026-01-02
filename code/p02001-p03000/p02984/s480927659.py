import math,itertools,fractions,heapq,collections,bisect,sys,queue,copy

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7
dd=[(-1,0),(0,1),(1,0),(0,-1)]
ddn=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return input()

def main():
  # Xi+Xi+1=2Ai
  # Xi=S-(Xi+1+Xi+2...)
  # X1=S-2A2-2A4...

  n=I()
  l=LI()
  sm=sum(l)
  _a=0
  for i,x in enumerate(l):
    if i%2==1:
      _a+=x
  x1=sm-_a*2
  ans=[x1]
  for i in range(n-1):
    b=2*l[i]-x1
    x1=b
    ans.append(x1)
  return ' '.join([str(x) for x in ans])

# main()
print(main())
