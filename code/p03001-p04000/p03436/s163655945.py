height, width = map(int, input().split(" "))
grids = list()
grids_accessed = list()
whites = 0
for h in range(height):
    inputted = input()
    whites += inputted.count(".")
    grids.append(list(inputted))
    grids_accessed.append([False]*len(inputted))


def get_next(x, y):
    nexts = ((x-1, y),
             (x+1, y),
             (x, y-1),
             (x, y+1))
    for x, y in nexts:
        if (0 <= x <= width-1) and (0 <= y <= height-1):
            if grids[y][x] == ".":
                yield x, y


def dfs():
    queue = list()
    x, y = 0, 0
    queue.append((x, y))
    while True:
        try:
            x, y = queue.pop(0)
        except IndexError:
            return
        if x == width-1 and y == height-1:
            return
        for n_x, n_y in get_next(x, y):
            if grids_accessed[n_y][n_x] is False:
                grids_accessed[n_y][n_x] = (x, y)
                queue.append((n_x, n_y))


def get_shortest():
    x, y = width-1, height-1
    distance_traveled = 0
    while True:
        if x == 0 and y == 0:
            return distance_traveled
        else:
            x, y = grids_accessed[y][x]
            distance_traveled += 1


dfs()
if grids_accessed[height-1][width-1] is False:
    print(-1)
else:
    d = get_shortest() + 1
    score = whites - d
    if score < 0:
        score = -1
    print(score)
