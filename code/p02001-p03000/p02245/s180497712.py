from sys import stdin
readline = stdin.readline


adjacent = (
    (1, 3),        # 0
    (0, 2, 4),     # 1
    (1, 5),        # 2
    (0, 4, 6),     # 3
    (1, 3, 5, 7),  # 4
    (2, 4, 8),     # 5
    (3, 7),        # 6
    (4, 6, 8),     # 7
    (5, 7)         # 8
)


def next_board(board, space, prev):
    for nxt in adjacent[space]:
        if nxt == prev:
            continue
        b = board[:]
        b[space], b[nxt] = b[nxt], 0
        yield b, nxt
from heapq import heappop, heappush

end = [1, 2, 3, 4, 5, 6, 7, 8, 0]

# ???????????¨????????°
FORE = 1
BACK = 0


def search(start):
    if start == end:
        return 0
    table = {}

    table[tuple(start)] = (FORE, 0)
    table[tuple(end)] = (BACK, 0)

    heap = [(0, start, start.index(0), None, FORE), (0, end, end.index(0), None, BACK)]
    while heap:
        i, board, space, prev, direction = heappop(heap)
        i += 1
        for b, nxt in next_board(board, space, prev):
            key = tuple(b)
            if key in table:
                if table[key][0] != direction:
                    return table[key][1] + i
                continue
            table[key] = (direction, i)
            if b == end:
                return i
            heappush(heap, (i, b, nxt, space, direction))


def main():
    start = (map(int, readline().split()) for _ in range(3))
    start = [y for x in start for y in x]
    print(search(start))
main()