import unittest
import collections


class TestD(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think(['...', '...', '...']), 4)

    def test_2(self):
        self.assertEqual(think(['...#.', '.#.#.', '.#...']), 10)


def solve():
    maze = read()
    result = think(maze)
    write(result)


def read():
    h, w = read_int(2)
    maze = []
    for _ in range(h):
        maze.append(read_line(n=w))
    return maze


def read_int(n):
    return read_type(int, n, sep=' ')


def read_float(n):
    return read_type(float, n, sep=' ')


def read_type(t, n, sep):
    return list(map(lambda x: t(x), read_line().split(sep)))[:n]


def read_line(n=0):
    if n == 0:
        return input().rstrip()
    else:
        return input().rstrip()[:n]


def think(maze):
    wall = '#'
    h, w = get_height_and_width_of(maze)
    longest_path_length = 0

    for y in range(h):
        for x in range(w):
            if maze[y][x] == wall:
                continue
            longest_path_length = max(longest_path_length, search(maze, x, y, wall))

    return longest_path_length


def write(result):
    print(result)


def get_height_and_width_of(maze):
    return len(maze), len(maze[0])


def search(maze, x, y, wall):
    h, w = get_height_and_width_of(maze)
    inf = h * w + 1

    dp = prepare_dp_table(h, w, inf)

    return bfs(maze, dp, w, h, x, y, wall)


def prepare_dp_table(h, w, inf):
    return [[inf for _ in range(w)] for _ in range(h)]


def bfs(maze, dp, w, h, x, y, wall):
    queue = collections.deque([])
    queue.append((x, y, 0))

    max_distance = 0

    diff_xy = [
        (-1, 0), (1, 0), (0, -1), (0, 1)
    ]

    while queue:
        xx, yy, distance = queue.popleft()
        if dp[yy][xx] <= distance:
            continue
        dp[yy][xx] = distance
        max_distance = max(max_distance, distance)

        for dx, dy in diff_xy:
            nx, ny = xx + dx, yy + dy
            if not in_range(w, h, nx, ny):
                continue
            if maze[ny][nx] == wall:
                continue
            if dp[ny][nx] <= distance + 1:
                continue
            queue.append((nx, ny, distance + 1))

    return max_distance


def in_range(w, h, x, y):
    return 0 <= x < w and 0 <= y < h


if __name__ == '__main__':
    # unittest.main()
    solve()