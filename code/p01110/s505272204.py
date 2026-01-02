from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,datetime
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inpl(): return list(map(int, input().split()))
def inpl_str(): return list(input().split())


def rev_w(MAP,H,W):
    nextMAP = [[] for y in range(H)]
    for y in range(H):
        nextMAP[y] = MAP[y][::-1]
    return nextMAP

def rev_h(MAP,H,W):
    nextMAP = [[0]*W for y in range(H)]
    for y in range(H):
        for x in range(W):
            nextMAP[y][x] = MAP[H-y-1][x]
    return nextMAP

while True:
    W,H,t,p = inpl()
    if W == 0:
        break
    else:
        MAP = [[1]*W for y in range(H)]
        for _ in range(t):
            d,c = inpl()
            if d == 1:
                if W//2 >= c:
                    hanten = False
                else:
                    hanten = True

                if hanten:
                    MAP = rev_w(MAP,H,W)
                    c = W - c

                nextW = W - c
                nextH = H
                nextMAP = [[1]*nextW for y in range(H)]
                for y in range(H):
                    for x in range(c):
                        nextMAP[y][x] = MAP[y][x+c] + MAP[y][(c-1)-x]
                    for x in range(c,nextW):
                        nextMAP[y][x] = MAP[y][x+c]

            elif d == 2:
                if H//2 >= c:
                    hanten = False
                else:
                    hanten = True

                if hanten:
                    MAP = rev_h(MAP,H,W)
                    c = H - c

                nextW = W
                nextH = H - c
                nextMAP = [[1]*W for y in range(nextH)]
                for x in range(W):
                    for y in range(c):
                        nextMAP[y][x] = MAP[y+c][x] + MAP[(c-1)-y][x]
                    for y in range(c,nextH):
                        nextMAP[y][x] = MAP[y+c][x]

            MAP = nextMAP
            H,W = nextH,nextW

        for _ in range(p):
            x,y = inpl()
            print(MAP[y][x])

