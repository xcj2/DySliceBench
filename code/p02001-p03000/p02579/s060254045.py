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
  H,W=LI()
  Ch,Cw=LI()
  Dh,Dw=LI()
  Ch-=1
  Cw-=1
  Dh-=1
  Dw-=1
  field=[S() for _ in range(H)]

  q=collections.deque()
  q2=collections.deque()
  q.append((Ch,Cw,0))
  ans=[[inf]*W for _ in range(H)]
  while True:
    if not q:
      if not q2:
        break
      else:
        q=q2
        q2=collections.deque()
    # for x in ans:
    #   print(x)
    # print()
    y,x,cnt=q.popleft()
    if ans[y][x]<=cnt:
      continue
    ans[y][x]=cnt
    if y==Dh and x==Dw:
      continue

    for dy,dx in dd:
      ny=y+dy
      nx=x+dx

      if 0<=ny<H and 0<=nx<W:
        if field[ny][nx]=='.':
          q.append((ny,nx,cnt))
        else:
          if dy==1 and dx==0:
            for i in range(0,2):
              for j in range(-2,3):
                nny=ny+i
                nnx=nx+j
                if 0<=nny<H and 0<=nnx<W:
                  if field[nny][nnx]=='.':
                    if ans[nny][nnx]>cnt+1:
                      q2.append((nny,nnx,cnt+1))
          elif dy==0 and dx==1:
            for i in range(-2,3):
              for j in range(0,2):
                nny=ny+i
                nnx=nx+j
                if 0<=nny<H and 0<=nnx<W:
                  if field[nny][nnx]=='.':
                    if ans[nny][nnx]>cnt+1:
                      q2.append((nny,nnx,cnt+1))
          elif dy==-1 and dx==0:
            for i in range(-1,1):
              for j in range(-2,3):
                nny=ny+i
                nnx=nx+j
                if 0<=nny<H and 0<=nnx<W:
                  if field[nny][nnx]=='.':
                    if ans[nny][nnx]>cnt+1:
                      q2.append((nny,nnx,cnt+1))
          elif dy==0 and dx==-1:
            for i in range(-2,3):
              for j in range(-1,1):
                nny=ny+i
                nnx=nx+j
                if 0<=nny<H and 0<=nnx<W:
                  if field[nny][nnx]=='.':
                    if ans[nny][nnx]>cnt+1:
                      q2.append((nny,nnx,cnt+1))

  x=ans[Dh][Dw]
  if x==inf:
    return -1
  return x

# main()
print(main())
