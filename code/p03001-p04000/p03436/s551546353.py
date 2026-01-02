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
    def find_path(p0, p1):
        queue = deque()
        footsteps = dict()

        queue.append((p0, 0))

        while queue:
            p, s = queue.popleft()
            footsteps[p] = s

            if p == p1:
                return s

            for pp in [(p[0] + 1, p[1]), (p[0] - 1, p[1]), (p[0], p[1] + 1), (p[0], p[1] - 1)]:
                if 0 <= pp[0] < width and 0 <= pp[1] < height and field[pp[1]][pp[0]] == '.' and pp not in footsteps:
                    queue.append((pp, s + 1))
                    footsteps[pp] = -1  # placeholder

        return -1

    height, width = tuple(input_ints())
    field = [input() for _ in range(height)]

    s = find_path((0, 0), (width - 1, height - 1))

    if s < 0:
        return -1
    else:
        return "".join(field).count(".") - (s + 1)


def main():
    print(solve())


main()
