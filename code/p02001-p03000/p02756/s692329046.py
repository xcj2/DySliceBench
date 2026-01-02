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
  s=list(S())
  s=collections.deque(s)
  f=True
  q=I()

  for _ in range(q):
    l=LS()
    if l==['1']:
      f=not f
    else:
      if l[1]=='1':
        if f:
          s.appendleft(l[2])
        else:
          s.append(l[2])
      else:
        if f:
          s.append(l[2])
        else:
          s.appendleft(l[2])

  s=list(s)

  if f:
    return ''.join(s)
  s.reverse()
  return ''.join(s)

# main()
print(main())
