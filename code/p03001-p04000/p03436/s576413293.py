def solve():
    s = read()
    result = think(s)
    write(result)


def read():
    h, w = read_int(2)
    s = []
    for y in range(h):
        s.append(list(read_line(w)))
    return s


def read_int(n):
    return list(map(int, read_line().split(' ')))[:n]


def read_line(n=0):
    if n == 0:
        return input().rstrip()
    else:
        return input().rstrip()[:n]


def think(s):
    w, h = get_area(s)
    gx, gy = w - 1, h - 1

    invalid = w * h
    white_tile_mark = '.'

    memo = bfs(s, w, h, white_tile_mark, invalid)

    if memo[gy][gx] == invalid:
        return -1

    shortest_path = get_shortest_path(memo, w, h, gx, gy)
    white_tiles = collect_tiles(s, white_tile_mark)
    score = 0

    for w in white_tiles:
        if w not in shortest_path:
            score += 1
    return score


def get_area(s):
    w = len(s[0])
    h = len(s)
    return w, h


def bfs(s, w, h, white_tile_mark, invalid):
    sx, sy = 0, 0

    memo = [[invalid for x in range(w)] for y in range(h)]
    queue = []
    queue.append([sx, sy, 0])

    next_steps = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    while queue:
        nx, ny, nd = queue.pop(0)
        if not (0 <= nx < w and 0 <= ny < h and s[ny][nx] == white_tile_mark and memo[ny][nx] > nd):
            continue
        memo[ny][nx] = nd

        for dx, dy in next_steps:
            queue.append([nx + dx, ny + dy, nd + 1])
    return memo


def get_shortest_path(memo, w, h, gx, gy):
    next_steps = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    shortest_path = []
    cx, cy = gx, gy

    while True:
        shortest_path.append([cx, cy])
        current_distance = memo[cy][cx]
        if current_distance == 0:
            break
        for dx, dy in next_steps:
            nx, ny = cx + dx, cy + dy
            if not (0 <= nx < w and 0 <= ny < h):
                continue
            if memo[ny][nx] == current_distance - 1:
                cx, cy = nx, ny
                break

    return shortest_path


def collect_tiles(s, mark):
    w, h = get_area(s)
    tiles = []
    for y in range(h):
        for x in range(w):
            if s[y][x] == mark:
                tiles.append([x, y])
    return tiles


def write(result):
    print(result)


if __name__ == '__main__':
    solve()