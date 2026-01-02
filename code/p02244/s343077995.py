def put_queen(board, pr, pc):
    def check_square(r, c):
        tmp = (pr == r) + (pc == c)
        if tmp:
            return tmp
        return 1 if abs(pr - r) == abs(pc - c) else board[r][c]

    return list(list(check_square(r, c) for c in range(8)) for r in range(8))


def check_board(board):
    return sum(sum(row) for row in board) == 72


def draw_board(board):
    print('\n'.join(''.join('Q' if c == 2 else '.' for c in row) for row in board))


def search_place(board):
    for r, row in enumerate(board):
        for c, square in enumerate(row):
            if square == 0:
                if search_place(put_queen(board, r, c)):
                    return True
    if check_board(board):
        draw_board(board)
        return True
    else:
        return False


n = int(input())
board = list(list(0 for c in range(8)) for r in range(8))

for _ in range(n):
    r, c = map(int, input().split())
    board = put_queen(board, r, c)

search_place(board)