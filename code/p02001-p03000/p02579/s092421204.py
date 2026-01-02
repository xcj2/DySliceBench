# import sys
# input = sys.stdin.readline

def mp(): return map(int, input().split())
def lmp(): return list(map(int, input().split()))

h,w = mp()
ch, cw = mp()
dh,dw = mp()
ch += 1
cw += 1
dh += 1
dw += 1
grid = []
grid.append(["#"]*(w+4))
grid.append(["#"]*(w+4))
ans_grid = []
for i in range(h):
    u = ["#", "#"]
    a = list(input())
    for j in range(w):
        u.append(a[j])
    u.append("#")
    u.append("#")
    grid.append(u)
grid.append(["#"]*(w+4))
grid.append(["#"]*(w+4))

for i in range(h+4):
    ans_grid.append([int(1e6+2)]*(w+4))
# print(grid)
# print(ans_grid)

from collections import deque
def bfs(x,y):
    q = deque([])
    used = set()
    q.append((x,y))
    used.add((x,y))
    ans_grid[x][y] = 0
    while q:
        here = q.popleft()
        move = [(here[0]-1, here[1]),
                (here[0], here[1]-1),
                (here[0], here[1]+1),
                (here[0]+1, here[1])]
        warp = [(here[0]-2, here[1]-2), (here[0]-2, here[1]-1), (here[0]-2, here[1]), (here[0]-2, here[1]+1), (here[0]-2, here[1]+2),
                (here[0]-1, here[1]-2), (here[0]-1, here[1]-1), (here[0]-1, here[1]+1), (here[0]-1, here[1]+2),
                (here[0], here[1]-2), (here[0], here[1]+2),
                (here[0]+1, here[1]-2), (here[0]+1, here[1]-1), (here[0]+1, here[1]+1), (here[0]+1, here[1]+2),
                (here[0]+2, here[1]-2), (here[0]+2, here[1]-1), (here[0]+2, here[1]), (here[0]+2, here[1]+1), (here[0]+2, here[1]+2)]
        for i in range(len(warp)):
            u = warp[i][0]
            v = warp[i][1]
            if grid[u][v] == "." and ans_grid[u][v] > ans_grid[here[0]][here[1]]+1:
                ans_grid[u][v] = min(ans_grid[u][v], ans_grid[here[0]][here[1]]+1)
                q.append((u,v))
        for i in range(len(move)):
            u = move[i][0]
            v = move[i][1]
            if (move[i] not in used or ans_grid[u][v] > ans_grid[here[0]][here[1]]) and grid[u][v] == ".":
                ans_grid[u][v] = min(ans_grid[here[0]][here[1]], ans_grid[u][v])
                q.appendleft((u,v))
                used.add((u,v))

bfs(ch,cw)
ans = ans_grid[dh][dw]
# print(ans_grid)
if ans == int(1e6+2):
    print(-1)
else:
    print(ans)


