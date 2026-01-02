import sys,collections

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
  field=[S() for _ in range(h)]

  ans=0
  visited=[[-1 for __ in range(w)] for _ in range(h)]
  q=collections.deque()
  for i in range(h):
    for j in range(w):
      if field[i][j]=='#':
        continue
      q.append((i,j))
      for _i in range(h):
        for _j in range(w):
          visited[_i][_j]=-1
      visited[i][j]=0
      _ans=0
      while q:
        y,x=q.popleft()

        for dy,dx in ((-1,0),(0,1),(1,0),(0,-1)):
          ny=y+dy
          nx=x+dx
          if not 0<=ny<h:
            continue
          if not 0<=nx<w:
            continue
          if field[ny][nx]=='#':
            continue
          if visited[ny][nx]!=-1:
            continue
          _ans=visited[y][x]+1
          visited[ny][nx]=_ans
          q.append((ny,nx))
      ans=max(ans,_ans)
  return ans

# main()
print(main())
