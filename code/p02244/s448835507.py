import copy


def is_vaild(board, i, j):
    if "Q" in board[i]:
        return False

    for k in range(8):
        if board[k][j] == "Q":
            return False

    # fill cross(left-up)
    m, n = i - 1, j - 1
    while m >= 0 and n > 0:
        if board[m][n] == "Q":
            return False
        m -= 1
        n -= 1

    # fill cross(left-down)
    m, n = i + 1, j - 1
    while m < 8 and n >= 0:
        if board[m][n] == "Q":
            return False
        m += 1
        n -= 1

    # fill cross(right-down)
    m, n = i + 1, j + 1
    while m < 8 and n < 8:
        if board[m][n] == "Q":
            return False
        m += 1
        n += 1

    # fill cross(right-up)
    m, n = i - 1, j + 1
    while m >= 0 and n < 8:
        if board[m][n] == "Q":
            return False
        m -= 1
        n += 1

    return True


def fill_board(board, i, j):
    if not is_vaild(board, i, j):
        return

    # fill row
    for k in range(8):
        board[i][k] = "."

    # fill column
    for k in range(8):
        board[k][j] = "."

    # fill cross(left-up)
    m, n = i - 1, j - 1
    while m >= 0 and n >= 0:
        board[m][n] = "."
        m -= 1
        n -= 1

    # fill cross(left-down)
    m, n = i + 1, j - 1
    while m < 8 and n >= 0:
        board[m][n] = "."
        m += 1
        n -= 1

    # fill cross(right-down)
    m, n = i + 1, j + 1
    while m < 8 and n < 8:
        board[m][n] = "."
        m += 1
        n += 1

    # fill cross(right-up)
    m, n = i - 1, j + 1
    while m >= 0 and n < 8:
        board[m][n] = "."
        m -= 1
        n += 1

    board[i][j] = "Q"
    return


def helper(board, rem):
    if rem == 0:
        for line in board:
            print("".join(line))
        quit()

    for i in range(8):
        for j in range(8):
            if board[i][j] == "#" and is_vaild(board, i, j):
                _prev = copy.deepcopy(board)
                fill_board(board, i, j)
                helper(board, rem - 1)
                board = _prev  # BackTracking
    return


board = [["#"] * 8 for _ in range(8)]

K = int(input())
flag = False
for _ in range(K):
    i, j = [int(i) for i in input().split()]
    if board[i][j] == "#" and is_vaild(board, i, j):
        fill_board(board, i, j)


helper(board, 8 - K)

