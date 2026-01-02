import sys,collections;sys.setrecursionlimit(10**7)
def Is(): return [int(x) for x in sys.stdin.readline().split()]
def Ss(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

def debug_print(maze):
    for xx in maze:
        for yy in xx:
            print(yy,end="")
        print("\n",end="")

def clear_maze(sx, sy, gx, gy, maze):
#    debug_print(maze)
    INF = 100000000
    field_x_length = len(maze)
    field_y_length = len(maze[0])
    distance = [[INF for i in range(field_y_length)] for j in range(field_x_length)]
    def bfs():
        queue = []
        queue.insert(0, (sx, sy))
        distance[sx][sy] = 0
        while len(queue):
            x, y = queue.pop()
            if x == gx and y == gy:
                break
            for i in range(0, 4):
                nx, ny = x + [1, 0, -1, 0][i], y + [0, 1, 0, -1][i]
                if (0 <= nx and nx < field_x_length and 0 <= ny and ny < field_y_length and maze[nx][ny] != '#' and distance[nx][ny] == INF):
                    queue.insert(0, (nx, ny))
                    distance[nx][ny] = distance[x][y] + 1
        if distance[H-1][W-1] == INF:
            print(-1)
            exit()
        return distance[gx][gy] 
    return bfs()

H,W = Is()
maze = []
for _ in range(H):
    maze.append(list(S()))
sx, sy = 0, 0 # スタート地点の座標
gx, gy = H-1, W-1 # ゴール地点の座標
a = clear_maze(sx, sy, gx, gy, maze)
for i in range(H):
    a += maze[i].count("#")
print(H*W-a-1)
