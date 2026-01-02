n = int(input())
nt = []

board = [["." for _ in range(8)] for _ in range(8)]

for i in range(n):
    y, x = map(int, input().split())
    board[y][x] = "Q"
    nt.append(y)

def output():
    for row in board:
        print("".join(row), sep=None)

def check(x, y):
    for i in range(8):
        for j in range(8):
            if i == y and j == x:
                continue
            elif i == y and board[i][j] == "Q":
                return False
            elif j == x and board[i][j] == "Q":
                return False
            elif abs(i-y) == abs(j-x) and board[i][j] == "Q":
                return False
    return True

def dfs(row):
    if row == 8:
        output()
        return
    if row in nt:
        dfs(row+1)
        return

    for i in range(8):
        board[row][i] = "Q"
        if not check(i, row):
            board[row][i] = "."
            continue
        else:
            dfs(row+1)
            board[row][i] = "."


dfs(0)