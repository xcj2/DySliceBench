def examB():
    W, H, N = LI()
    height = [0,H]; width = [0,W]
    for i in range(N):
        x, y, a = LI()
        if a==1:
            width[0] = max(width[0],x)
        elif a==2:
            width[1] = min(width[1],x)
        elif a==3:
            height[0] = max(height[0],y)
        elif a==4:
            height[1] = min(height[1],y)
    ans = max(width[1]-width[0],0)*max(height[1]-height[0],0)
    print(ans)

import sys
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examB()