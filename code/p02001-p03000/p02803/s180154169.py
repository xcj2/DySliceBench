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
    mz = [input() for i in range(h)]

    from collections import deque

    ret = 0
    for x in range(h):
        for y in range(w):
            # 壁からはスタートできない
            if mz[x][y] == "#":
                continue

            # 初期化
            distance = [[0] * w for _ in range(h)]
            # start位置
            dq = deque([[x, y]])

            while dq:
                now_h, now_w = dq.popleft()
                for i, j in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    new_h, new_w = now_h + i, now_w + j
                    if new_h < 0 or new_w < 0 or new_h >= h or new_w >= w:
                        continue

                    if mz[new_h][new_w] != "#" and distance[new_h][new_w] == 0:
                        distance[new_h][new_w] = distance[now_h][now_w] + 1
                        dq.append([new_h, new_w])

            distance[x][y] = 0
            ret = max(max(list(map(max, distance))), ret)

    return ret


if __name__ == "__main__":
    print(main())
