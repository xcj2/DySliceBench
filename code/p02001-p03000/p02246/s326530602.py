from sys import stdin
readline = stdin.readline


GOAL = [i for i in range(1, 16)] + [0]
MAX_DEPTH = 45  # 80
count = 0

# ??£??\?????????
adjacent = (
    (1, 4),          # 0
    (0, 2, 5),       # 1
    (1, 6, 3),       # 2
    (2, 7),          # 3
    (0, 5, 8),       # 4
    (1, 4, 6, 9),    # 5
    (2, 5, 7, 10),   # 6
    (3, 6, 11),      # 7
    (4, 9, 12),      # 8
    (5, 8, 10, 13),  # 9
    (6, 9, 11, 14),  # 10
    (7, 10, 15),     # 11
    (8, 13),         # 12
    (9, 12, 14),     # 13
    (10, 13, 15),    # 14
    (11, 14)         # 15
)

# ???????????????????????¢
distance = (
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 1, 2, 3, 1, 2, 3, 4, 2, 3, 4, 5, 3, 4, 5, 6),
    (1, 0, 1, 2, 2, 1, 2, 3, 3, 2, 3, 4, 4, 3, 4, 5),
    (2, 1, 0, 1, 3, 2, 1, 2, 4, 3, 2, 3, 5, 4, 3, 4),
    (3, 2, 1, 0, 4, 3, 2, 1, 5, 4, 3, 2, 6, 5, 4, 3),
    (1, 2, 3, 4, 0, 1, 2, 3, 1, 2, 3, 4, 2, 3, 4, 5),
    (2, 1, 2, 3, 1, 0, 1, 2, 2, 1, 2, 3, 3, 2, 3, 4),
    (3, 2, 1, 2, 2, 1, 0, 1, 3, 2, 1, 2, 4, 3, 2, 3),
    (4, 3, 2, 1, 3, 2, 1, 0, 4, 3, 2, 1, 5, 4, 3, 2),
    (2, 3, 4, 5, 1, 2, 3, 4, 0, 1, 2, 3, 1, 2, 3, 4),
    (3, 2, 3, 4, 2, 1, 2, 3, 1, 0, 1, 2, 2, 1, 2, 3),
    (4, 3, 2, 3, 3, 2, 1, 2, 2, 1, 0, 1, 3, 2, 1, 2),
    (5, 4, 3, 2, 4, 3, 2, 1, 3, 2, 1, 0, 4, 3, 2, 1),
    (3, 4, 5, 6, 2, 3, 4, 5, 1, 2, 3, 4, 0, 1, 2, 3),
    (4, 3, 4, 5, 3, 2, 3, 4, 2, 1, 2, 3, 1, 0, 1, 2),
    (5, 4, 3, 4, 4, 3, 2, 3, 3, 2, 1, 2, 2, 1, 0, 1)
)


def manhattan_distance(board):
    return sum(distance[bi][i] for i, bi in enumerate(board))


def answer_is_odd(board):
    return sum(divmod(board.index(0), 4)) % 2


def search(board):
    lower = manhattan_distance(board)
    start_depth = lower
    if (lower % 2) ^ answer_is_odd(board):
        start_depth += 1
    for limit in range(start_depth, MAX_DEPTH + 1, 2):
        id_lower_search(board, limit, 0, board.index(0), None, lower)
        if count > 0:
            return limit


def nxt_board(board, space, prev):
    for nxt in adjacent[space]:
        if nxt == prev:
            continue
        b = board[:]
        b[space], b[nxt] = b[nxt], 0
        yield b, nxt


def id_lower_search(board, limit, move, space, prev, lower):
    if move == limit:
        if board == GOAL:
            global count
            count += 1
    else:
        for b, nxt in nxt_board(board, space, prev):
            p = board[nxt]
            new_lower = lower - distance[p][nxt] + distance[p][space]
            if new_lower + move <= limit:
                id_lower_search(b, limit, move + 1, nxt, space, new_lower)


def main():
    start = (map(int, readline().split()) for _ in range(4))
    start = [y for x in start for y in x]
    print(search(start))
main()