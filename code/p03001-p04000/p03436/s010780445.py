from collections import deque

WHITE = -1
BLACK = -2
GOAL = -3
field_mapping = {
    '.': WHITE,
    '#': BLACK
}


def neighbors(y, x):
    points = []
    if y-1 >= 0:
        points.append([y-1, x])
    if y+1 < H:
        points.append([y+1, x])
    if x-1 >= 0:
        points.append([y, x-1])
    if x+1 < W:
        points.append([y, x+1])
    return points


def searching():
    field[0][0] = 1
    queue = deque([[0, 0]])
    while len(queue) > 0:
        [y, x] = queue.popleft()
        current_distance = field[y][x]
        for [n_y, n_x] in neighbors(y, x):
            point_status = field[n_y][n_x]
            if point_status == WHITE:
                field[n_y][n_x] = current_distance + 1
                queue.append([n_y, n_x])
            elif point_status == GOAL:
                return current_distance + 1
    return -1


def main():
    global H, W, field
    [H, W] = [int(i) for i in input().split()]
    field = []
    white_num = 0
    for i in range(H):
        line = []
        for color in [field_mapping[s] for s in input()]:
            line.append(color)
            if color == WHITE:
                white_num += 1
        field.append(line)
    field[H-1][W-1] = GOAL
    walked_points = searching()
    if walked_points < 0:
        print(-1)
    else:
        print(white_num - walked_points)


if __name__ == '__main__':
    main()
