

def is_symmetric(board):
    for i in range(N):
        for j in range(i, N):
            if board(j, i) != board(i, j):
                return False
    return True


def translate(board, a, b):
    def get(i, j):
        return board[(i + a) % N][(j + b) % N]
    
    return get


def solve(board):
    ans = 0
    for a in range(N):
        if is_symmetric(translate(board, a, 0)):
            ans += N - a
    for b in range(N):
        if b == 0:
            continue
        if is_symmetric(translate(board, 0, b)):
            ans += N - b
    return ans


N = int(input())
board = []
for i in range(N):
    board.append(input())


print(solve(board))