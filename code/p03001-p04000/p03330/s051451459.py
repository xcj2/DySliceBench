import sys
# sys.setrecursionlimit(100000)
from collections import Counter


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    n, c = input_int_list()
    grid = []
    discomfort = []

    for _ in range(c):
        discomfort.append(input_int_list())

    for _ in range(n):
        grid.append(input_int_list())

    c0 = []
    c1 = []
    c2 = []

    # 色を揃えるマスを1次配列に振り分け
    for i in range(n):
        for j in range(n):
            if (i + j + 2) % 3 == 0:
                c0.append(grid[i][j])
            elif (i + j + 2) % 3 == 1:
                c1.append(grid[i][j])
            else:
                c2.append(grid[i][j])

    # それぞれを集計
    c0 = Counter(c0)
    c1 = Counter(c1)
    c2 = Counter(c2)

    ans = float("inf")

    # 塗り分けを全パターン試す
    for x in range(1, c + 1):
        for y in range(1, c + 1):
            for z in range(1, c + 1):
                if x == y or y == z or z == x:
                    continue
                tmp = 0
                for k, v in c0.items():
                    if k == x:
                        continue
                    else:
                        tmp += discomfort[k - 1][x - 1] * v

                for k, v in c1.items():
                    if k == y:
                        continue
                    else:
                        tmp += discomfort[k - 1][y - 1] * v

                for k, v in c2.items():
                    if k == z:
                        continue
                    else:
                        tmp += discomfort[k - 1][z - 1] * v

                ans = min(ans, tmp)

    print(ans)

    return


if __name__ == "__main__":
    main()
