import math,itertools,fractions,heapq,bisect,sys,queue,copy

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
  q=[]

  field=[S() for _ in range(h)]
  counter=[[inf]*w for _ in range(h)]

  sharp_cnt=0
  for x in field:
    sharp_cnt+=x.count('#')

  q.append((0,0,1))

  while len(q)>0:
    y,x,cnt=q.pop()
    if counter[y][x]<cnt:
      continue
    counter[y][x]=cnt

    for dy,dx in dd:
      ny=y+dy
      nx=x+dx

      if 0<=ny and 0<=nx and ny<h and nx<w:
        if field[ny][nx]!='#':

          if counter[ny][nx]>cnt+1:
            q.append((ny,nx,cnt+1))

  step_cnt=counter[h-1][w-1]

  if step_cnt==inf:
    return -1

  return h*w-sharp_cnt-step_cnt

# main()
print(main())
