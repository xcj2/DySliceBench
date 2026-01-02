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

    def get_right_face_index(self, upper: int, front: int) -> int:
        for i, num in enumerate(self.sur[upper]):
            if num == front:
                return self.sur[upper][(i + 1) % 4]
        else:
            raise ValueError('get_right_faceの来てはいけない箇所')

    def get_num(self, index) -> int:
        return self.s[index]

    def get_sur_index(self, num) -> int:
        for i in range(len(self.s)):
            if num == self.s[i]:
                return i
        else:
            raise ValueError('get_sur_indexの来てはいけない箇所')


# 提出用
data = [int(i) for i in input().split()]
N = int(input())
dice = Dice(data)
for _i in range(N):
    upper_num, right_num = map(int, input().split())
    upper_index = dice.get_sur_index(upper_num)
    right_index = dice.get_sur_index(right_num)
    ans_index = dice.get_right_face_index(upper_index, right_index)
    print(dice.get_num(ans_index))

# # 動作確認用
# with open('input_itp1_11_a_1.txt', mode='r', encoding='utf8') as fin:
#     data = [int(i) for i in next(fin).split()]
#     N = int(next(fin))
#     dice = Dice(data)
#     for _i in range(N):
#         upper_num, right_num = map(int, next(fin).split())
#         upper_index = dice.get_sur_index(upper_num)
#         right_index = dice.get_sur_index(right_num)
#         ans_index = dice.get_right_face_index(upper_index, right_index)
#         print(dice.get_num(ans_index))

