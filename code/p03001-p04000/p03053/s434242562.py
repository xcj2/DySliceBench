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
  h,w=LI()
  field=[list(S()) for _ in range(h)]
  d=0

  q=collections.deque()
  nokori=h*w
  dist=[[-1]*w for _ in range(h)]
  for i in range(h):
    for j in range(w):
      if field[i][j]=='#':
        q.append((i,j))
        dist[i][j]=0
        nokori-=1

  while q:
    if nokori==0:
      return d

    y,x=q.popleft()

    for dy,dx in dd:
      ny=y+dy
      nx=x+dx

      if 0<=ny and ny<h and 0<=nx and nx<w:
        if field[ny][nx]=='.':
          field[ny][nx]='#'
          d=dist[y][x]+1
          dist[ny][nx]=d
          q.append((ny,nx))
          nokori-=1

  return d

# main()
print(main())
