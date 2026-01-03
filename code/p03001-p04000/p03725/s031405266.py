#!usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS():return [list(x) for x in sys.stdin.readline().split()]
def S():
    res = list(sys.stdin.readline())
    if res[-1] == "\n":
        return res[:-1]
    return res
def IR(n):
    return [I() for i in range(n)]
def LIR(n):
    return [LI() for i in range(n)]
def SR(n):
    return [S() for i in range(n)]
def LSR(n):
    return [LS() for i in range(n)]

sys.setrecursionlimit(1000000)
mod = 1000000007

#A
def A():
    def f(n):
        return ((1<<n)-(1-2*(n&1)))//3
    def k(x,n):
        return f(n)*s+(1-2*(n&1))*x
    a = LI()
    if a[0]%2 or a[1]%2 or a[2]%2:
        print(0)
        return
    if a[0] == a[1] == a[2]:
        print(-1)
        return
    s = sum(a)
    ans = 10**5
    for i in range(3):
        l = 0
        r = 10**5+1
        while r-l > 1:
            m = (l+r)>>1
            ka = k(a[i],m)
            if ka&((1<<m)-1) == 0:
                l = m
            else:
                r = m
        ans = min(ans, l)
    print(ans)
    return
#B
def B():
    n,m = LI()
    f = [0]*n
    for i in range(m):
        a,b = LI()
        f[a-1] ^= 1
        f[b-1] ^= 1
    if all([not f[i]%2 for i in range(n)]):
        print("YES")
    else:
        print("NO")
    return

#C
def C():
    d = [(1,0),(-1,0),(0,1),(0,-1)]
    h,w,k = LI()
    a = SR(h)
    for y in range(h):
        for x in range(w):
            if a[y][x] == "S":
                sy,sx = y,x
                break
    bfs = [[-1]*w for i in range(h)]
    bfs[sy][sx] = 0
    q = deque([(sy,sx)])
    while q:
        y,x = q.popleft()
        for dy,dx in d:
            ny,nx = y+dy,x+dx
            if 0 <= ny < h and 0 <= nx < w:
                if a[ny][nx] == "#":
                    continue
                if bfs[ny][nx] < 0:
                    bfs[ny][nx] = bfs[y][x]+1
                    if bfs[ny][nx] < k:
                        q.append((ny,nx))

    ans = float("inf")
    for y in range(h):
        for x in range(w):
            if bfs[y][x] >= 0:
                ans = min(ans, y, h-1-y, x, w-1-x)
    print(math.ceil(ans/k)+1)
    return

#D
def D():

    return

#E
def E():

    return

#F
def F():

    return

#Solve
if __name__ == "__main__":
    C()
