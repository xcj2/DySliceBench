import collections
import itertools

H, W = map(int, input().split())
s = [list(input()) for _ in range(H)]


def is_white(i, j):
    return i in range(H) and j in range(W) and s[i][j] == "."


def adjacent_white_squares(i, j):
    return [
        (i + di, j + dj)
        for di, dj in [(0, -1), (0, 1), (-1, 0), (1, 0)]
        if is_white(i + di, j + dj)
    ]


def distance_to_goal():
    distances = [[-1 for _ in range(W)] for _ in range(H)]
    distances[0][0] = 0
    queue = collections.deque([(0, 0)])

    d = 0
    while queue:
        i, j = queue.popleft()
        to_visit = [
            (k, l) for k, l in adjacent_white_squares(i, j) if distances[k][l] == -1
        ]
        for k, l in to_visit:
            if (k, l) == (H - 1, W - 1):
                return distances[i][j] + 1

            distances[k][l] = distances[i][j] + 1
            queue.append((k, l))

    return -1


def black_squares():
    return sum(1 for c in itertools.chain.from_iterable(s) if c == "#")


distance = distance_to_goal()
if distance == -1:
    print(-1)
else:
    print(H * W - (distance + 1) - black_squares())
