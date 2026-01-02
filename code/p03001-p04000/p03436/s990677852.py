from collections import deque
from itertools import chain


class Solver:
    def __init__(self, m):
        self.m = m
        self.label = [[-1 for _ in range(len(m[0]))] for _ in range(len(m))]

    def bfs(self, s, g):
        queue = deque()
        start = [a - 1 for a in s]
        goal = [a - 1 for a in g]
        queue.append(start)
        self.label[start[0]][start[1]] = 0
        while len(queue) > 0:
            node = queue.popleft()
            y, x = node
            dist = self.label[y][x] + 1
            if y > 0:
                if self.m[y - 1][x] != "#" and self.label[y - 1][x] == -1:
                    if y-1 == goal[0] and x == goal[1]:
                        return dist
                    else:
                        queue.append([y - 1, x])
                        self.label[y - 1][x] = dist
            if y < len(self.m)-1:
                if self.m[y + 1][x] != "#" and self.label[y + 1][x] == -1:
                    if y+1 == goal[0] and x == goal[1]:
                        return dist
                    else:
                        queue.append([y + 1, x])
                        self.label[y + 1][x] = dist
            if x > 0:
                if self.m[y][x - 1] != "#" and self.label[y][x - 1] == -1:
                    if y == goal[0] and x-1 == goal[1]:
                        return dist
                    else:
                        queue.append([y, x-1])
                        self.label[y][x-1] = dist
            if x < len(self.m[0])-1:
                if self.m[y][x + 1] != "#" and self.label[y][x + 1] == -1:
                    if y == goal[0] and x+1 == goal[1]:
                        return dist
                    else:
                        queue.append([y, x+1])
                        self.label[y][x + 1] = dist
        return -1


def main():
    H, W = list(map(int, input().split()))
    m = [list(input()) for _ in range(H)]
    sum = list(chain.from_iterable(m)).count(".")

    solver = Solver(m)
    ans = solver.bfs([1, 1], [H, W])
    if ans == -1:
      print(-1)
      quit()
    print(sum - ans -1)


if __name__ == "__main__":
    main()
