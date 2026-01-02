def main():
    b = []
    line = input().split(" ")
    H = int(line[0])
    W = int(line[1])
    for l in range(H):
        b.append(input())

    result = []
    for i, line in enumerate(b):
        result_row = ""
        for j, c in enumerate(line):
            if c == ".":
                n = count(i, j, b, H, W)
                result_row += str(n)
            else:
                result_row += b[i][j]
        result.append(result_row)

    for l in result:
        print(l)


def count(row, column, board, H, W):
    n = 0
    rs, re = judge_row(row, H)
    cs, ce = judge_col(column, W)
    for r in range(rs, re):
        for c in range(cs, ce):
            if board[r][c] == "#":
                n += 1
    return n


def judge_row(row, H):
    if H == 1:
        return 0, 1
    elif row == 0:
        return row, row+1+1 
    elif row == H-1:
        return row-1, row+1
    else:
        return row-1, row+1+1


def judge_col(col, W):
    if W == 1:
        return 0, 1
    elif col == 0:
        return col, col+1+1 
    elif col == W-1:
        return col-1, col+1
    else:
        return col-1, col+1+1


if __name__ == "__main__":
    main()
