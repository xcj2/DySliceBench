import copy

dirs = [[-1, -1], [-1, 0], [-1, 1],
        [0, -1], [0, 1],
        [1, -1], [1, 0], [1, 1]]

def place(board, r, c):
    if board[r][c] != '.':
        return False
    board[r][c] = 'Q'
    for d in dirs:
        rr = r + d[0]
        cc = c + d[1]
        while rr >= 0 and rr < 8 and cc >= 0 and cc < 8:
            board[rr][cc] = 'x'
            rr += d[0]
            cc += d[1]
    return True

def solve(board_):
    board = copy.deepcopy(board_)
    for r in range(8):
        for c in range(8):
            if place(board, r, c):
                tmp = solve(board)
                if tmp:
                    return tmp
                else:
                    board = copy.deepcopy(board_)
    if sum([row.count('Q') for row in board]) == 8:
        return board

def disp(board, clean=False):
    for row in board:
        if clean:
            row = ['.' if i == 'x' else i for i in row]
        print(''.join(row))

board = [['.'] * 8 for i in range(8)]
N = int(input())
for _ in range(N):
    r, c = map(int, input().split())
    place(board, r, c)

board = solve(board)

disp(board, True)


