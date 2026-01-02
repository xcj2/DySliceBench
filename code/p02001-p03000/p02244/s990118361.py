import sys
from itertools import permutations


def in_board(r, c):
    return 0 <= r < 8 and 0 <= c < 8


def reachable_generator(r, c):
    # 斜め(左上-右下)
    i = 1
    while True:
        if not in_board(r - i, c - i):
            break
        yield r - i, c - i
        i += 1
    i = 1
    while True:
        if not in_board(r + i, c + i):
            break
        yield r + i, c + i
        i += 1
    # 斜め(右上-左下)
    i = 1
    while True:
        if not in_board(r - i, c + i):
            break
        yield r - i, c + i
        i += 1
    i = 1
    while True:
        if not in_board(r + i, c - i):
            break
        yield r + i, c - i
        i += 1


def solve(ini):
    for p in permutations(range(8)):
        s = set()
        for i, j in enumerate(p):
            s.add((i, j))
        if not ini <= s:
            continue
        for i, j in s:
            for k, l in reachable_generator(i, j):
                if (k, l) in s:
                    break
            else:
                continue
            break
        else:
            return s


def main():
    input = sys.stdin.buffer.readline
    k = int(input())
    # ini:初期条件
    ini = set()
    for _ in range(k):
        r, c = map(int, input().split())
        ini.add((r, c))
    s = solve(ini)

    board = [["."] * 8 for _ in range(8)]
    for i, j in s:
        board[i][j] = "Q"
    for i in range(8):
        print("".join(board[i]))


if __name__ == "__main__":
    main()

