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

    directions = ((1, 0), (0, 1), (-1, 0), (0, -1))

    for i in range(1, h + 1):
        for j in range(1 + w + 1):
            # "#"の周りに１つでも"#"がつながっていないか調べる
            if grid[i][j] == "#":
                cnt = 0
                for x, y in directions:
                    if grid[i + x][j + y] == "#":
                        cnt += 1
                if cnt == 0:
                    print("No")
                    return
    print("Yes")
    return


if __name__ == "__main__":
    main()
