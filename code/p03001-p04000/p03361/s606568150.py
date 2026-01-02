import sys
from itertools import product

sys.setrecursionlimit(200000)


def input():
    return sys.stdin.readline()[:-1]


def ii(t: type = int):
    return t(input())


def il(t: type = int):
    return list(map(t, input().split()))


def imi(N: int, t: type = int):
    return [ii(t) for _ in range(N)]


def iml(N: int, t: type = int):
    return [il(t) for _ in range(N)]


class PathFinder:
    def __init__(self, num_dst, border):
        if num_dst == 4:
            self.dx = (-1, 0, 0, 1)
            self.dy = (0, -1, 1, 0)
        elif num_dst == 8:
            self.dx = (-1, -1, -1, 0, 0, 1, 1, 1)
            self.dy = (-1, 0, 1, -1, 1, -1, 0, 1)
        self.border = border

    # 周辺探索
    def find_neighbours(self, current_x, current_y):
        for neighbour in zip(self.dx, self.dy):
            neighbour_x = current_x + neighbour[0]
            neighbour_y = current_y + neighbour[1]
            if (
                self.border[0] <= neighbour_x < self.border[1]
                and self.border[2] <= neighbour_y < self.border[3]
            ):
                yield neighbour_x, neighbour_y


def solve():

    H, W = il()
    S = imi(H, str)
    finder = PathFinder(4, (0, H, 0, W))
    for i, j in product(range(H), range(W)):
        flag = 0
        for x, y in finder.find_neighbours(i, j):
            if S[i][j] == "#" and S[x][y] == ".":
                flag += 1
        if flag == 4:
            return "No"
    return "Yes"


if __name__ == "__main__":
    print(solve())
