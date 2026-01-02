import sys
from typing import List


class Dice:

    def __init__(self, values: List[int]):
        self.face_value = values

    def get_value(self, face_num) -> int:
        return self.face_value[face_num]

    def get_all_values(self) -> str:
        return ' '.join(map(str, self.face_value))

    def get_upper_value(self) -> int:
        return self.get_value(0)

    def invoke_method(self, mkey: str) -> None:
        if mkey == 'S':
            self.S()
        elif mkey == 'N':
            self.N()
        elif mkey == 'E':
            self.E()
        elif mkey == 'W':
            self.W()
        else:
            raise ValueError(f'This method does not exist. : {mkey}')

    def set_value(self, s0, s1, s2, s3, s4, s5) -> None:
        self.face_value[0] = s0
        self.face_value[1] = s1
        self.face_value[2] = s2
        self.face_value[3] = s3
        self.face_value[4] = s4
        self.face_value[5] = s5

    def S(self) -> None:
        self.set_value(self.face_value[4], self.face_value[0],
                       self.face_value[2], self.face_value[3],
                       self.face_value[5], self.face_value[1])

    def N(self) -> None:
        self.set_value(self.face_value[1], self.face_value[5],
                       self.face_value[2], self.face_value[3],
                       self.face_value[0], self.face_value[4])

    def E(self) -> None:
        self.set_value(self.face_value[3], self.face_value[1],
                       self.face_value[0], self.face_value[5],
                       self.face_value[4], self.face_value[2])

    def W(self) -> None:
        self.set_value(self.face_value[2], self.face_value[1],
                       self.face_value[5], self.face_value[0],
                       self.face_value[4], self.face_value[3])

    def R(self) -> None:
        """横回転."""
        self.set_value(self.face_value[0], self.face_value[2],
                       self.face_value[4], self.face_value[1],
                       self.face_value[3], self.face_value[5])


def check_R(dice1, dice2) -> bool:
    """横回転をチェックする."""
    for _i in range(4):
        dice1.R()
        if dice1.get_all_values() == dice2.get_all_values():
            return True
    return False


# 提出用
data1 = [int(i) for i in input().split()]
data2 = [int(i) for i in input().split()]

# # 動作確認用1
# with open('input_itp1_11_c_2.txt', mode='r', encoding='utf8') as fin:
#     data1 = [int(i) for i in next(fin).split()]
#     data2 = [int(i) for i in next(fin).split()]

dice1 = Dice(data1)
dice2 = Dice(data2)


for _i in range(4):
    dice1.S()
    if dice1.get_upper_value() == dice2.get_upper_value():
        if check_R(dice1, dice2):
            print('Yes')
            sys.exit()

for _i in range(4):
    dice1.E()
    if dice1.get_upper_value() == dice2.get_upper_value():
        if check_R(dice1, dice2):
            print('Yes')
            sys.exit()

print('No')
