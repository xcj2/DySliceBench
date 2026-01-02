from itertools import permutations

BLANK = 0
Q = 1
WALL = 2

def to_board_pos(x, y):
    return x * 10 + y

def place_queen(pos, board):
    assert board[pos] != WALL
    if board[pos] == Q:
        return False, None

    board[pos] = Q
    directions = [-10, -9, 1, 11, 10, 9, -1, -11]
    for d in directions:
        restrict_board(pos, d, board)
    
    return True, board

def restrict_board(pos, direction, board):
    cur = pos+direction
    while board[cur] != WALL:
        board[cur] = Q
        cur += direction

def check(pattern, board):
    b = board[:]
    for i, p in enumerate(pattern):
        ok, b = place_queen(to_board_pos(i+1, p), b)
        if not ok:
            return False

    return True

def print_board(board):
    for i in range(10):
        for j in range(10):
            pos = to_board_pos(i, j)
            print(str(board[pos]) + " ", end="")
        print("")

    
n = int(input())
initial_queens = [(0, 0) for i in range(n)]
for i in range(n):
    x, y = map(int, input().split())
    initial_queens[i] = (x, y)

board = [BLANK] * 100
for i, _ in enumerate(board):
    if 0 <= i <= 9 or 90 <= i <= 99:
        board[i] = WALL
        continue

    if i % 10 == 0 or i % 10 == 9:
        board[i] = WALL
        continue

perm_seed = [i+1 for i in range(8)]
patterns = permutations(perm_seed)

ans = [0] * 8
for pattern in patterns:
    init_ok = True
    for iq in initial_queens:
        if pattern[iq[0]] != iq[1] + 1:
            init_ok = False
            break

    if init_ok:
        if check(pattern, board):
            ans = pattern
            break

for i, a in enumerate(ans):
    board[to_board_pos(i+1, a)] = Q

for i in range(1, 9):
    for j in range(1, 9):
        pos = to_board_pos(i, j)
        if board[pos] == BLANK:
            print(".", end="")
        elif board[pos] == Q:
            print("Q", end="")
    print("")
