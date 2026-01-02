def checkRows(grid):
    for row in grid:
        if all([n == True for n in row]):
            return True
    return False


def checkCols(grid):
    for j in range(3):
        if all([n == True for n in [grid[i][j] for i in range(3)]]):
            return True
    return False


def checkDiags(grid):
    return all([n == True for n in [grid[i][i] for i in range(3)]]) or \
           all([n == True for n in [grid[i][2 - i] for i in range(3)]])


if __name__ == '__main__':
    grid = [[0] * 3 for i in range(3)]
    idx = {}

    for i in range(3):
        grid[i] = [int(s) for s in input().strip().split()]
        for j in range(3):
            idx[grid[i][j]] = (i, j)

    n = int(input())
    bs = [-1] * n

    for i in range(n):
        bs[i] = int(input())
        if bs[i] in idx.keys():
            a, b = idx[bs[i]]
            grid[a][b] = True

    if checkRows(grid) or checkCols(grid) or checkDiags(grid):
        print("Yes")
    else:
        print("No")
