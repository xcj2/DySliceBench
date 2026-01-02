from collections import deque
HW = input().split()
H, W = int(HW[0]), int(HW[1])
C = input().split()
Ch, Cw = int(C[0]), int(C[1])
D = input().split()
Dh, Dw = int(D[0]), int(D[1])
route = []
for h in range(H):
    route.append(input())

visited = [[False]*W for x in range(H)]
kouho = deque()
kouho.append([Ch-1, Cw-1])
warpkouho = deque()

def check_walk(a, b):
    if 0 <= a <= H-1 and 0 <= b <= W-1: 
        if visited[a][b] == False and route[a][b] == ".":
            kouho.append([a, b])
def check_warp(a, b, cwarp):
    if 0 <= a <= H-1 and 0 <= b <= W-1:
        if visited[a][b] == False and route[a][b] == ".":
            warpkouho.append([a, b, cwarp+1])

def wizard():
    warp = 1
    while True:
        if len(kouho) != 0:
            tmp = kouho.popleft()
        elif len(warpkouho) != 0:
            tmp = warpkouho.popleft()
            warp = tmp[2]
        else:
            break
        h = tmp[0]
        w = tmp[1]
        if visited[h][w] == False:
            visited[h][w] = warp
            check_walk(h-1, w)
            check_walk(h+1, w)
            check_walk(h, w-1)
            check_walk(h, w+1)
            for n in range(5):
                for m in range(5):
                  check_warp(h-2+n, w-2+m, warp)
        if h == Dh-1 and w == Dw-1:
            print(visited[h][w]-1)
            return
    print(-1)
wizard()
        
        
