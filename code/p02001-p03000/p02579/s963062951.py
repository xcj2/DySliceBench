import sys
sys.setrecursionlimit(10**7)

readline = sys.stdin.buffer.readline
def readstr():return readline().rstrip().decode()
def readstrs():return list(readline().decode().split())
def readint():return int(readline())
def readints():return list(map(int,readline().split()))
def printrows(x):print('\n'.join(map(str,x)))
def printline(x):print(' '.join(map(str,x)))

import heapq
def dijkstra(s,path):
    # 距離をinfで初期化
    d = [float('inf')]*len(path)
    d[s] = 0

    # sへの距離は0
    q = [(0,s)]
    heapq.heapify(q)

    # 距離が最小の頂点から更新していけば良い
    while q:
        c,p = heapq.heappop(q)

        # 頂点pまでの距離がheap内のpまでの距離より小さい場合、continue
        if d[p]<c:
            continue

        # 頂点pから伸びる、全ての辺の距離を確認
        for to,cost in path[p]:
            # 頂点pから行ける頂点の距離がpまでの距離とpからの距離の和より小さい場合 -> 距離を更新し、heapに追加
            if d[to] > d[p] + cost:
                d[to] = d[p] + cost
                heapq.heappush(q,(d[to], to))
    return d

h,w = readints()

start = readints()
start = (start[0]-1)*w + start[1]-1

goal = readints()
goal = (goal[0]-1)*w + goal[1]-1

maze = [readstr() for i in range(h)]

path = [[] for i in range(h*w)]
for i in range(h*w):
    y = i//w
    x = i%w
    if maze[y][x]=='#':
        continue
    for dy in range(-2,3):
        for dx in range(-2,3):
            if dy==dx==0:
                continue
            if 0<=y+dy<h and 0<=x+dx<w and maze[y+dy][x+dx]=='.':
                j = (y+dy)*w + x+dx
                if (dy==0 and abs(dx)==1) or (abs(dy)==1 and dx==0):
                    path[i].append((j,0))
                else:
                    path[i].append((j,1))

d = dijkstra(start,path)
print(-1 if d[goal]==float('inf') else d[goal])
    






