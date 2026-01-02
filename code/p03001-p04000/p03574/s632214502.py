import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    h, w = input_int_list()
    grid = []
    grid.append(["."] * (w + 2))
    for _ in range(h):
        grid.append(["."] + list(input()) + ["."])
    grid.append(["."] * (w + 2))

    directions = ((1, 1), (0, 1), (1, 0), (-1, 0), (0, -1), (-1, -1), (-1, 1), (1, -1))

    for i in range(1, h + 1):
        for j in range(1, w + 1):
            cnt = 0
            # 周辺の爆弾を数える
            if grid[i][j] == ".":
                for x, y in directions:
                    if grid[i + x][j + y] == "#":
                        cnt += 1
                grid[i][j] = cnt

    for i in range(1, h + 1):
        print("".join(str(i) for i in grid[i][1:-1]))
    return


if __name__ == "__main__":
    main()
