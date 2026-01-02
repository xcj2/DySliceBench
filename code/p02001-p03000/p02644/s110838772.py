from collections import deque
import sys

int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def MI1(): return map(int1, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

def main():
    inf=10**9
    h,w,k=MI()
    x1,y1,x2,y2=MI1()
    aa=[[0 if c=="@" else inf for c in SI()] for _ in range(h)]
    #p2D(aa)

    aa[x1][y1]=0
    q=deque()
    q.append((x1,y1,0))
    while q:
        x,y,d=q.popleft()
        for nx in range(x+1,min(x+k+1,h)):
            if aa[nx][y] == d + 1:continue
            if aa[nx][y]<d+1:break
            aa[nx][y]=d+1
            q.append((nx,y,d+1))
        for nx in range(x-1,max(x-k-1,-1),-1):
            if aa[nx][y] == d + 1:continue
            if aa[nx][y]<d+1:break
            aa[nx][y]=d+1
            q.append((nx,y,d+1))
        for ny in range(y+1,min(y+k+1,w)):
            if aa[x][ny] == d + 1:continue
            if aa[x][ny]<d+1:break
            aa[x][ny]=d+1
            q.append((x,ny,d+1))
        for ny in range(y-1,max(y-k-1,-1),-1):
            if aa[x][ny] == d + 1:continue
            if aa[x][ny]<d+1:break
            aa[x][ny]=d+1
            q.append((x,ny,d+1))
        #p2D(aa)
        #print()

    ans=aa[x2][y2]
    if ans==inf:print(-1)
    else:print(ans)

main()