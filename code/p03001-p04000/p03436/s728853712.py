from collections import deque

class Map_input():

    def __init__(self):
        line = input().split(" ")
        self.H = int(line[0])
        self.W = int(line[1])
        Map = [[] for i in range(self.H)]
        for i in range(self.H):
            line = input()
            for j in range(self.W):
                if line[j] == ".":
                    Map[i].append(0)
                else:
                    Map[i].append(1)
        self.Map = Map

class Maze_min():
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    def __init__(self, H, W, Map, start, goal):
        self.H = H
        self.W = W
        self.Map = Map
        self.goal = goal
        self.queue = deque([start])
        self.dist = [[-1]*W for i in range(H)]
        self.dist[start[0]][start[1]] = 0

    def min_step(self):
        while len(self.queue) > 0:
            p = self.queue.popleft()
            if p == self.goal:
                break
            else:
                for i in range(len(Maze_min.dx)):
                    (nx, ny) = (p[0] + Maze_min.dx[i], p[1] + Maze_min.dy[i])
                    if nx in range(self.H) and ny in range(self.W) and self.Map[nx][ny] == 0 and self.dist[nx][ny] == -1:
                        self.queue.append((nx, ny))
                        self.dist[nx][ny] = self.dist[p[0]][p[1]] + 1
        return self.dist[self.goal[0]][self.goal[1]]

M = Map_input()
maze = Maze_min(M.H, M.W, M.Map, (0, 0), (M.H-1, M.W-1))
black_num = (sum(list(map(sum, M.Map))))
d = maze.min_step()
if d == -1:
    print(-1)
else:
    print(M.H*M.W - maze.min_step() - black_num -1)