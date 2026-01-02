class BreadthFirstSearch:

    def __init__(self, h, w, maze):
        self.h = h
        self.w = w
        self.maze = maze
        self.visited = [[0] * w for _ in range(h)]
        self.queue = []
        self.dx_dy = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        self.ans = 0

    def search(self):
        for i in range(self.h):
            for j in range(self.w):
                if self.maze[i][j] != ".":
                    continue
                self.queue.append((i, j))
                self.visited[i][j] = 1

                while len(self.queue) > 0:
                    now = self.queue.pop(0)
                    for dx, dy in self.dx_dy:
                        x = now[0] + dx
                        y = now[1] + dy
                        if x < 0 or self.h <= x:
                            continue
                        if y < 0 or self.w <= y:
                            continue
                        if self.maze[x][y] == "#":
                            continue
                        if self.visited[x][y] == 0:
                            self.visited[x][y] = self.visited[now[0]][now[1]] + 1
                            self.queue.append((x, y))
                for l in range(self.h):
                    for m in range(self.w):
                        self.ans = max(self.ans, self.visited[l][m])
                self.queue = []
                self.visited = [[0] * self.w for _ in range(self.h)]


def main():
    h, w = map(int, input().split())
    maze = [list(input()) for _ in range(h)]
    bfs = BreadthFirstSearch(h, w, maze)
    bfs.search()
    print(bfs.ans-1)


if __name__ == "__main__":
    main()
