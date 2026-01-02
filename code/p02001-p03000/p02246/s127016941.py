from sys import stdin
from heapq import heappush, heappop
solution = [i for i in range(1, 16)] + [0]
sol_idx = (15, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)
MAX_DEPTH = 45
count = 0
neighbor = (
    (1, 4),
    (0, 2, 5),
    (1, 6, 3),
    (2, 7),
    (0, 5, 8),
    (1, 4, 6, 9),
    (2, 5, 7, 10),
    (3, 6, 11),
    (4, 9, 12),
    (5, 8, 10, 13),
    (6, 9, 11, 14),
    (7, 10, 15),
    (8, 13),
    (9, 12, 14),
    (10, 13, 15),
    (11, 14)
)
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
    (5, 4, 3, 4, 4, 3, 2, 3, 3, 2, 1, 2, 2, 1, 0, 1),
    (6, 5, 4, 3, 5, 4, 3, 2, 4, 3, 2, 1, 3, 2, 1, 0)
)
def get_diff(B):
    return sum(distance[v][i] for i, v in enumerate(B))
def get_next_board(board, space, prev):
    for nxt in neighbor[space]:
        if nxt == prev: continue
        b = board[:]
        b[space], b[nxt] = b[nxt], 0
        yield b, nxt
def answer_is_odd(board):
    return sum(divmod(board.index(0), 4)) % 2
def search(board):
    lower = get_diff(board)
    start_depth = lower
    if (lower % 2) ^ answer_is_odd(board): start_depth += 1
    for limit in range(start_depth, MAX_DEPTH + 1, 2):
        get_next(board, limit, 0, board.index(0), None, lower)
        if count > 0: return limit
def get_next(board, limit, move, space, prev, lower):
    if move == limit:
        if board == solution:
            global count
            count += 1
    else:
        for b, nxt in get_next_board(board, space, prev):
            p = board[nxt]
            new_lower = lower - distance[p][nxt] + distance[p][space]
            if new_lower + move <= limit:
                get_next(b, limit, move + 1, nxt, space, new_lower)
print(search([int(a) for _ in range(4) for a in stdin.readline().split()]))