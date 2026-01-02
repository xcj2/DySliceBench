
def read_input():
    h, w = map(int, input().split())
    slist = []
    for i in range(h):
        slist.append(input().strip())

    return h, w, slist

# i, jの周辺に1を足す
def sumup(board, i, j):
    def notbomb(x):
        return x != '#'

    up = i - 1 >= 0
    down = i + 1 < len(board)
    left = j - 1 >= 0
    right = j + 1 < len(board[0])

    if up:
        if notbomb(board[i - 1][j]):
            board[i - 1][j] += 1
        if left:
            if notbomb(board[i - 1][j - 1]):
                board[i - 1][j - 1] += 1
        if right:
            if notbomb(board[i - 1][j + 1]):
                board[i - 1][j + 1] += 1
    if left:
        if notbomb(board[i][j - 1]):
            board[i][j - 1] += 1
    if right:
        if notbomb(board[i][j + 1]):
           board[i][j + 1] += 1
    if down:
        if notbomb(board[i + 1][j]):
            board[i + 1][j] += 1
        if left:
            if notbomb(board[i + 1][j - 1]):
                board[i + 1][j - 1] += 1
        if right:
            if notbomb(board[i + 1][j + 1]):
                board[i + 1][j + 1] += 1
    return board

def submit():
    h, w, slist = read_input()

    board = []
    for s in slist:
        board.append([0 if c == '.' else c for c in s])

    for i in range(h):
        for j in range(w):
            if board[i][j] == '#':
                board = sumup(board, i, j)

    for row in board:
        print(''.join([str(c) for c in row]))


if __name__ == '__main__':
    submit()