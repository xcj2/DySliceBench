import sys
import math
from collections import defaultdict, deque
from copy import deepcopy
    
input = sys.stdin.readline
def RD(): return input().rstrip()
def F(): return float(input().rstrip())
def I(): return int(input().rstrip())
def MI(): return map(int, input().split())
def MF(): return map(float,input().split())
def LI(): return list(map(int, input().split()))
def LF(): return list(map(float,input().split()))
def Init(H, W, num): return [[num for i in range(W)] for j in range(H)]
    
    
def main():
    H, W = MI()
    sx, sy = MI()
    gx, gy = MI()
    sx-=1
    sy-=1
    gx-=1
    gy-=1
    
    mylist = [input().rstrip() for i in range(H)]
    dist = Init(H, W, float('inf'))
    #dist2 = Init(H, W, float('inf'))
    dq = deque()
    dq2 = deque()
    dq.append((sx, sy))
    move1 = [[1,0],[0,1],[-1,0],[0,-1]]
    move2 = [[i,j] for i in range(-2,3) for j in range(-2,3) if not [i, j ] in move1 and [i, j] != [0, 0]]
    dist[sx][sy] = 0
    while dq:
        x, y = dq.popleft()
        if x == gx and y == gy:
            print(dist[gx][gy])
            sys.exit()


        #コスト1の移動
        for x2, y2 in move2:
            x2 += x
            y2 += y
            if x2 >= 0 and x2 < H and y2 >= 0 and y2 < W and mylist[x2][y2] == "." and dist[x2][y2] > dist[x][y]+1:
                dist[x2][y2] = dist[x][y]+1
                dq2.append((x2,y2))

        #コスト0の移動
        for x2, y2 in move1:
            x2 += x
            y2 += y
            if x2 >= 0 and x2 < H and y2 >= 0 and y2 < W and mylist[x2][y2] == "." and dist[x2][y2] > dist[x][y]:
                dist[x2][y2] = dist[x][y]
                dq.append((x2,y2))

        if not dq:
            dq = deque(set(dq2))
            dq2 = deque()
        
    
    if dist[gx][gy] == float('inf'):
        print(-1)
    else:
        print(dist[gx][gy])
    
if __name__ == "__main__":
    main()