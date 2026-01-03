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
  s=list(S())

  a1=list('dream')
  a2=list('dreamer')
  a3=list('erase')
  a4=list('eraser')

  while len(s)>4:
    if s[-5:]==a1:
      for _ in range(5):
        s.pop()
    elif s[-7:]==a2:
      for _ in range(7):
        s.pop()
    elif s[-5:]==a3:
      for _ in range(5):
        s.pop()
    elif s[-6:]==a4:
      for _ in range(6):
        s.pop()
    else:
      break

  if s==[]:
    return 'YES'
  return 'NO'

# main()
print(main())
