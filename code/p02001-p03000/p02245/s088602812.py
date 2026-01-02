import sys
from heapq import heappop, heappush


adjacent = (
    (1, 3),        # 位置 0 に 0が存在したときに入れ替え可能な位置
    (0, 2, 4),     # 位置 1 に 0が存在したときに入れ替え可能な位置
    (1, 5),        # 位置 2 に 0が存在したときに入れ替え可能な位置
    (0, 4, 6),     # 位置 3 に 0が存在したときに入れ替え可能な位置
    (1, 3, 5, 7),  # 位置 4 に 0が存在したときに入れ替え可能な位置
    (2, 4, 8),     # 位置 5 に 0が存在したときに入れ替え可能な位置
    (3, 7),        # 位置 6 に 0が存在したときに入れ替え可能な位置
    (4, 6, 8),     # 位置 7 に 0が存在したときに入れ替え可能な位置
    (5, 7)         # 位置 8 に 0が存在したときに入れ替え可能な位置
)


def move(board, space, prev_space):
    for next_space in adjacent[space]:
        if next_space == prev_space:
            continue
        next_board = board[:]
        next_board[space], next_board[next_space] = next_board[next_space], 0
        yield next_board, next_space


end = [1, 2, 3, 4, 5, 6, 7, 8, 0]
discovered_state = set()  # すでに知っている状態を記録する


def search(start):
    discovered_state.add(tuple(start))
    heap = [(0, start, start.index(0), None)]  # 今の状態へ到達する手順回数

    while heap:
        i, board, space, prev = heappop(heap)

        if board == end:
            return i

        i += 1
        for next_board, next_space in move(board, space, prev):
            if tuple(next_board) in discovered_state:
                continue
            discovered_state.add(tuple(next_board))
            heappush(heap, (i, next_board, next_space, space))


def main():
    start = []
    for _ in range(3):
        start.extend(list(map(int, sys.stdin.readline().strip().split())))
    ans = search(start)
    print(ans)


if __name__ == '__main__':
    main()



