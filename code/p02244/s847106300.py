row, col = [True] * 8, [True] * 8
d_pos, d_neg = [True] * 15, [True] * 15
board = [["."] * 8 for _ in range(8)]


def change_state(r: int, c: int, undo: bool = False) -> None:
    if undo:
        row[r] = col[c] = d_pos[r + c] = d_neg[r - c + 7] = True
        board[r][c] = "."
    else:
        row[r] = col[c] = d_pos[r + c] = d_neg[r - c + 7] = False
        board[r][c] = "Q"


def solve_eight_queens(r: int = 0) -> None:
    while r < 8 and not row[r]:
        r += 1
    if r == 8:
        for board_row in board:
            print(*board_row, sep="")
        return
    for c in range(8):
        if not col[c] or not d_pos[r + c] or not d_neg[r - c + 7]:
            continue
        change_state(r, c)
        solve_eight_queens(r + 1)
        change_state(r, c, undo=True)


def main():
    K, *RC = map(int, open(0).read().split())
    for r, c in zip(*[iter(RC)] * 2):
        row[r] = col[c] = d_pos[r + c] = d_neg[r - c + 7] = False
        board[r][c] = "Q"
    solve_eight_queens()


if __name__ == "__main__":
    main()

