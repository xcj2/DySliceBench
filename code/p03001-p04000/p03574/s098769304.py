def solve():
    board = read()
    result = think(board)
    write(result)


def read():
    h, w = read_int(2)
    board = []
    for y in range(h):
        board.append(read_line(w))
    return board


def read_int(n):
    return list(map(lambda x: int(x), read_line().split(' ')))[:n]


def read_line(n=0):
    if n == 0:
        return input().rstrip()
    else:
        return input().rstrip()[:n]


def think(board):
    # destructive method
    vacant_cell_symbol = '.'
    bomber_cell_symbol = '#'

    x_range, y_range = get_xy_range(board)

    new_board = [[0 for x in range(x_range)] for y in range(y_range)]

    for y in range(y_range):
        for x in range(x_range):
            if board[y][x] == bomber_cell_symbol:
                new_board[y][x] = bomber_cell_symbol
            else:
                cells = gather_cells_around(board, x, y)
                new_board[y][x] = cells.count(bomber_cell_symbol)
    return new_board


def get_xy_range(board):
    return len(board[0]), len(board)


def gather_cells_around(board, x, y):
    x_range, y_range = get_xy_range(board)
    offsets = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    cells = []
    for offset in offsets:
        if on_board(offset, x, y, x_range, y_range):
            cells.append(board[y + offset[1]][x + offset[0]])
    return cells


def on_board(offset, x, y, x_range, y_range):
    return 0 <= x + offset[0] < x_range and 0 <= y + offset[1] < y_range


def write(result):
    for line in result:
        print(''.join(list(map(lambda x: str(x), line))))

if __name__ == '__main__':
    solve()