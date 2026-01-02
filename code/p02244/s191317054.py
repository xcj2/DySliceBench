num_queen = 8

def check_puttable(candidate, queens):
    cx, cy = candidate
    for queen in queens:
        qx, qy = queen
        if cx == qx or cy == qy or abs(cx - qx) == abs(cy - qy):
            return False
    return True

def create_candidates(queens):
    return [(i, j) for i in range(num_queen) for j in range(num_queen)
            if check_puttable((i,j), queens)]

def add_queen(queens):
    if len(queens) == num_queen: return queens
    candidates = create_candidates(queens)
    for candidate in candidates:
        _queens = add_queen(queens | {candidate})
        if _queens: return _queens

def show_queens(queens):
    for i in range(num_queen):
        for j in range(num_queen):
            if (i, j) in queens:
                print("Q", end="")
            else:
                print(".", end="")
        print("")

N = int(input())
queens = set()
for _ in range(N):
    i, j = map(int, input().split())
    queens.add((i, j))

queens = add_queen(queens)
show_queens(queens)

