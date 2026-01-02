# -*- coding: utf-8 -*-


# 入力を整数に変換して受け取る
def input_int():
    return int(input())


# マイナス1した値を返却
def int1(x):
    return int(x) - 1


# 半角スペース区切り入力をIntに変換してMapで受け取る
def input_to_int_map():
    return map(int, input().split())


# 半角スペース区切り入力をIntに変換して受け取る
def input_to_int_tuple():
    return tuple(map(int, input().split()))


# 半角スペース区切り入力をIntに変換してマイナス1した値を受け取る
def input_to_int_tuple_minus1():
    return tuple(map(int1, input().split()))


def main():
    h, w = input_to_int_map()
    zone = [input() for i in range(h)]

    from collections import deque
    black_cell = deque()

    black_distance = [[-1] * w for i in range(h)]
    for i, row in enumerate(zone):
        for j, cell in enumerate(row):
            if cell == "#":
                black_cell.append((i, j))
                black_distance[i][j] = 0

    while black_cell:
        black_h, black_w = black_cell.popleft()
        pre_black_distance = black_distance[black_h][black_w]
        for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            move_h = black_h + i
            move_w = black_w + j
            if move_h < 0 or move_w < 0 or move_h >= h or move_w >= w:
                continue
            if black_distance[move_h][move_w] == -1:
                black_distance[move_h][move_w] = pre_black_distance + 1
                black_cell.append((move_h, move_w))

    return max(list(map(max, black_distance)))


if __name__ == "__main__":
    print(main())
