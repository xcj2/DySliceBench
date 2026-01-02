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
    n, m = input_to_int_map()
    ab = [input_to_int_tuple() for i in range(m)]

    from collections import defaultdict
    room = defaultdict(set)
    for a, b in ab:
        room[a].add(b)
        room[b].add(a)


    from collections import deque
    root = deque()
    root.append(1)
    moved = [-1] * n
    moved[0] = 0
    while root:
        room_no = root.popleft()
        for move_room_no in room[room_no]:
            if moved[move_room_no - 1] != -1:
                continue

            root.append(move_room_no)
            moved[move_room_no - 1] = room_no

    if min(moved) == -1:
        print("No")
    else:
        print("Yes")
        for i in moved[1:]:
            print(i)


if __name__ == "__main__":
    main()
