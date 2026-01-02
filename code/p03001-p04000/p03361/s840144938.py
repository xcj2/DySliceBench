

def read_input():
    h, w = map(int, input().split())
    board = []

    for i in range(h):
        s = [c for c in input().strip()]
        board.append(s)

    return h, w, board


# マス(i, j)の上下左右のいずれかに黒が居るかどうか調べる
def check_neighbor(board, i, j):
    if i - 1 >= 0:
        if board[i - 1][j] == '#':
            return True
    if i + 1 < len(board):
        if board[i + 1][j] == '#':
            return True

    if j - 1 >= 0:
        if board[i][j - 1] == '#':
            return True
    if j + 1 < len(board[i]):
        if board[i][j + 1] == '#':
            return True
    return False


def submit():
    h, w, board = read_input()

    for i in range(h):
        for j in range(w):
            if board[i][j] == '#' and not check_neighbor(board, i, j):
                print('No')
                return

    print('Yes')


if __name__ == '__main__':
    submit()
