

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    H, W = read_ints()
    table = []
    for _ in range(H):
        table.append(list(input()))
    frontier = []
    whites = H*W
    for i in range(H):
        for j in range(W):
            if table[i][j] == '#':
                frontier.append((i, j))
                whites -= 1
    count = 0
    while whites != 0:
        new_frontier = []
        for i, j in frontier:
            for i0, j0 in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= i0 < H and 0 <= j0 < W and table[i0][j0] == '.':
                    table[i0][j0] = '#'
                    whites -= 1
                    new_frontier.append((i0, j0))
        frontier = new_frontier
        count += 1
    return count


if __name__ == '__main__':
    print(solve())
