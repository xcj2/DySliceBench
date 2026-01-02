import array
import itertools
from collections import defaultdict, deque


def log(s):
    # print("| " + str(s), file=sys.stderr)
    pass


def output(x):
    print(x, flush=True)


def input_ints():
    return map(int, input().split())


def solve():
    def fill(queue):
        footsteps = [[None] * width for _ in range(height)]

        for x, y in queue:
            footsteps[y][x] = 0

        s = 0
        while queue:
            queue2 = deque()
            s += 1
            while queue:
                x, y = queue.popleft()

                if x > 0 and footsteps[y][x - 1] is None:
                    queue2.append((x - 1, y))
                    footsteps[y][x - 1] = s
                if x < width - 1 and footsteps[y][x + 1] is None:
                    queue2.append((x + 1, y))
                    footsteps[y][x + 1] = s
                if y > 0 and footsteps[y - 1][x] is None:
                    queue2.append((x, y - 1))
                    footsteps[y - 1][x] = s
                if y < height - 1 and footsteps[y + 1][x] is None:
                    queue2.append((x, y + 1))
                    footsteps[y + 1][x] = s

            queue = queue2

        return s - 1

    height, width = tuple(input_ints())
    field = [input() for _ in range(height)]
    queue = deque()

    for y, line in enumerate(field):
        for x, c in enumerate(line):
            if c == '#':
                queue.append((x, y))
    # queue.append((10, 10))


    return fill(queue)


def main():
    print(solve())


main()
