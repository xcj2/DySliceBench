import sys

readline = sys.stdin.readline

def flatten_2dim(array):
    return [item for sublist in array for item in sublist]


def dfs(i, j):
    global flag, grid
    grid[i][j] = '.'
    if i == H and j == W:
        fgrid = flatten_2dim(grid)
        flag = ('#' in fgrid)
    if grid[i][j+1] == '#':
        dfs(i, j+1)
    if grid[i+1][j] == '#':
        dfs(i+1, j)
    grid[i][j] = '#'


def main():
    global H, W, grid, flag
    H, W = map(int, readline().split())
    grid = []
    grid.append(['.']*(W+2))
    for _ in range(H):
        grid.append(['.'] + list(readline()[:-1]) + ['.'])
    grid.append(['.']*(W+2))
    flag = True
    dfs(1, 1)

    if flag:
        print('Impossible')
    else:
        print('Possible')


if __name__ == "__main__":
    main()
