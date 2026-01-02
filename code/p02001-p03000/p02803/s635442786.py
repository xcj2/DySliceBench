import queue

class pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getter(self):
        return [self.x, self.y]

def solvmaiz(maze, x ,y):
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    q = queue.Queue()
    INF = 10**5
    d = [[INF for x in range(W)]for y in range(H)]
    q.put(pair(x,y))
    d[y][x] = 0
    goal = [0, 0]
    while(not q.empty()):
        p = q.get().getter()
        for i in range(4):
            nx = p[0] + dx[i]
            ny = p[1] + dy[i]
            if nx >= 0 and nx < W and ny >= 0 and ny < H and d[ny][nx] == INF and maze[ny][nx] != '#':
                q.put(pair(nx,ny))
                d[ny][nx] = d[p[1]][p[0]] + 1
        goal[0] = p[1]
        goal[1] = p[0]

    return d[goal[0]][goal[1]]

if __name__ == "__main__":
    H, W = map(int, input().split())
    maze =[]
    for i in range(H):
        j = input()
        maze.append([])
        for k in j:
            maze[i].append(k)
    ans = 0
    for y in range(H):
        for x in range(W):
            if maze[y][x] == '#':
                continue
            ans = max(ans, solvmaiz(maze, x, y))
    print(ans)