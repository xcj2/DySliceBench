from itertools import permutations
from heapq import heappop, heappush


def main():
    *A, = map(int, open(0).read().split())
    initial = get_hash(A)
    goal = get_hash([1, 2, 3, 4, 5, 6, 7, 8, 0])

    ans = search(initial, goal)
    print(ans)


def get_hash(A):
    board = 0
    for i, a in enumerate(A):
        board += a << i*4
    return board


def gen_move_table():
    mask = 0b1111
    dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    ret = [[] for _ in [0]*9]
    for y in range(3):
        for x in range(3):
            i = 3*y+x
            for dy, dx in dirs:
                dr = 3*dy+dx
                if 0 <= y+dy < 3 and 0 <= x+dx < 3:
                    sqmask = mask << (i+dr)*4
                    ret[i].append((dr, sqmask))
    return ret


def gen_next_board(board, move_table):
    mask = 0b1111
    ret = []
    for i in range(9):
        piece = board >> 4*i & mask
        if piece == 0:
            for move in move_table[i]:
                ret.append(do_move(board, move))
    return ret


def do_move(board, move):
    dr, sqmask = move

    sq = board & sqmask
    board ^= sq
    if dr > 0:
        board ^= sq >> dr*4
    else:
        board ^= sq << -dr*4

    return board


def heuristic(board):
    mask = 0b1111
    h = 0
    for i in range(9):
        y, x = divmod(i, 3)

        piece = board >> 4*i & mask
        if piece == 0:
            py, px = 2, 2
        else:
            py, px = divmod(piece-1, 3)
        h += abs(py-y)+abs(px-x)

    return h


def search(initial, goal):
    move_table = gen_move_table()

    dist = {}
    q = []

    dist[initial] = 0
    heappush(q, (heuristic(initial), 0, initial))
    while q:
        _, d, board = heappop(q)

        if board == goal:
            return d

        if board in dist and d > dist[board]:
            continue
        dist[board] = d

        for nboard in gen_next_board(board, move_table):
            nd = d + 1
            if (
                nboard not in dist or
                nboard in dist and nd < dist[nboard]
            ):
                heappush(q, (nd+heuristic(nboard), nd, nboard))


if __name__ == '__main__':
    main()

