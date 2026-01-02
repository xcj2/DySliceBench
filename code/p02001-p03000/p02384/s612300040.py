from typing import List


class Dice:

    sur = [i for i in range(6)]

    def __init__(self, s: List[int]):
        self.s = s  # surfaceリスト

        # indexが面の番号。リストの値は、それに接する面の番号。
        self.sur[0] = [1, 2, 4, 3]
        self.sur[1] = [0, 3, 5, 2]
        self.sur[2] = [1, 5, 4, 0]
        self.sur[3] = [1, 0, 4, 5]
        self.sur[4] = [0, 2, 5, 3]
        self.sur[5] = [1, 3, 4, 2]

    def get_right_face_num(self, upper_num: int, front_num: int) -> int:
        for i, value in enumerate(self.sur[upper_num]):
            if value == front_num:
                return self.sur[upper_num][(i + 1) % 4]
        else:
            raise ValueError('get_right_faceの来てはいけない箇所')

    def get_value(self, face_num) -> int:
        return self.s[face_num]

    def get_face_num(self, value) -> int:
        for i in range(len(self.s)):
            if value == self.s[i]:
                return i
        else:
            raise ValueError('get_sur_indexの来てはいけない箇所')


# 提出用
data = [int(i) for i in input().split()]
N = int(input())
dice = Dice(data)
for _i in range(N):
    upper_value, front_value = map(int, input().split())
    upper_num = dice.get_face_num(upper_value)
    front_num = dice.get_face_num(front_value)
    ans_num = dice.get_right_face_num(upper_num, front_num)
    print(dice.get_value(ans_num))

# # 動作確認用
# with open('input_itp1_11_a_1.txt', mode='r', encoding='utf8') as fin:
#     data = [int(i) for i in next(fin).split()]
#     N = int(next(fin))
#     dice = Dice(data)
#     for _i in range(N):
#         upper_value, front_value = map(int, next(fin).split())
#         upper_num = dice.get_face_num(upper_value)
#         front_num = dice.get_face_num(front_value)
#         ans_num = dice.get_right_face_num(upper_num, front_num)
#         print(dice.get_value(ans_num))

