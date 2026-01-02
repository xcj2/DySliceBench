import sys
from sys import stdin
def I():
    return stdin.readline().rstrip()
def MI():
    return map(int,stdin.readline().rstrip().split())
def LI():
    return list(map(int,stdin.readline().rstrip().split()))
#main part
from collections import deque
H,W=MI()
route=[list(I()) for _ in range(H)]
d=deque()
for h in range(H):
    for w in range(W):
        if route[h][w]=='#':
            d.append([h,w])
cnt=0
while d:
    l=list(d)
    d.clear()
    for Y,X in l:
        for y,x in [[Y-1,X],[Y+1,X],[Y,X-1],[Y,X+1]]:
            if 0<=y<H and 0<=x<W:
                if route[y][x]=='.':
                    route[y][x]='#'
                    d.append([y,x])
    cnt+=1
print(cnt-1)