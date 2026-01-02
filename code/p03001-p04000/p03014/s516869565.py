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
    for i in range(h):
        grid.append(list(input()))

    ver_cnt = [[None for _ in range(w)] for _ in range(h)]
    hor_cnt = [[None for _ in range(w)] for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if grid[i][j] == ".":
                # 横方向の数を埋める
                if not hor_cnt[i][j]:
                    j_end = j
                    cnt = 0
                    while j_end < w:
                        if grid[i][j_end] == "#":
                            break
                        else:
                            j_end += 1
                            cnt += 1
                    for _j in range(j, j_end):
                        hor_cnt[i][_j] = cnt
                # 縦方向の数を埋める
                if not ver_cnt[i][j]:
                    i_end = i
                    cnt = 0
                    while i_end < h:
                        if grid[i_end][j] == "#":
                            break
                        else:
                            i_end += 1
                            cnt += 1
                    for _i in range(i, i_end):
                        ver_cnt[_i][j] = cnt
    ans = 0

    for i in range(h):
        for j in range(w):
            if grid[i][j] != "#":
                ans = max(ans, ver_cnt[i][j] + hor_cnt[i][j] - 1)
    print(ans)


if __name__ == "__main__":
    main()
