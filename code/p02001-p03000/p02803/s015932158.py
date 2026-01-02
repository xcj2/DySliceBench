from collections import deque
import copy

def cha(maze,h,w):
    maze = copy.deepcopy(maze)
    for i in range(h):
        for j in range(w):
            if maze[i][j] == ".":
                maze[i][j] = 10**10
            if maze[i][j] == "#":
                maze[i][j] = -1
    return maze

def bfs(maze,sy,sx):
    maze = copy.deepcopy(maze)
    maze[sy][sx] = 0
    que = deque([[sy,sx]])
    while que:
        y,x = que.popleft()
        for next_y,next_x in [(y+1,x),(y-1,x),(y,x+1),(y,x-1)]:
            if maze[next_y][next_x] == -1:
                continue
            dist = maze[next_y][next_x]
            if dist > maze[y][x] + 1:
                maze[next_y][next_x] = maze[y][x] + 1
                que.append([next_y,next_x])
    return maze

def search(maze):
    c = 0
    for i in maze:
        i.append(c)
        c = max(i)
    return c

def _main():
    h,w = map(int,input().split())
    maze = [["#"]*w]
    for _ in range(h):
        maze.append(list(input()))
    maze.append(["#"]*w)
    for i in range(h+2):
        maze[i].insert(0,"#")
        maze[i].insert(w+1,"#")
    C = 0
    for sy in range(h+2):
        for sx in range(w+2):
            if maze[sy][sx] == ".":
                C = max((search(bfs(cha(maze,h+2,w+2),sy,sx)),C))
    print(C)

if __name__=="__main__":
    _main()

