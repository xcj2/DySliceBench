import sys

BLOCK_WIDTH = 4
BLOCK_HEIGHT = 2
field = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
w = 0
h = 0
xg = 0
yg = 0
start_color = 0

def main():
    global field, w, h, c, xg, yg, start_color
    while True:
        w, h = map(int, input().split())
        if w == 0 and h == 0:
            break
        xs, ys = map(int, input().split())
        xg, yg = map(int, input().split())
        xs -= 1
        ys -= 1
        xg -= 1
        yg -= 1
        n = int(input())
        field = [[0] * w for _ in range(h)]
        for i in range(n):
            c, d, x, y = map(int, input().split())
            arrangement(c, d, x - 1, y - 1)

        start_color = field[ys][xs]
        if dfs(xs, ys):
            print("OK")
        else:
            print("NG")


def arrangement(c, d, x, y):
    if d == 0:
        [[draw(x + j, y + i, c) for j in range(BLOCK_WIDTH)] for i in range(BLOCK_HEIGHT)]
    else:
        [[draw(x + j, y + i, c) for j in range(BLOCK_HEIGHT)] for i in range(BLOCK_WIDTH)]


def draw(x, y, c):
    global field
    field[y][x] = c


def dfs(x, y):
    global field

    if x == xg and y == yg:
        return True
    if start_color == 0:
        return False
    field[y][x] = 0
    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]
        if next_x < 0 or next_x >= w or next_y < 0 or next_y >= h:
            continue
        if field[next_y][next_x] != start_color:
            continue
        if dfs(next_x, next_y):
            return True

    return False


if __name__ == '__main__':
    main()