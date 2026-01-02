from typing import List


class Dice:

    def __init__(self, surface: List[int]):
        self.surface = surface

    def get_upper_sursurface(self) -> int:
        return self.surface[0]

    def invoke_method(self, mkey: str) -> None:
        if mkey == 'S':
            self.S()
            return None
        if mkey == 'N':
            self.N()
            return None
        if mkey == 'E':
            self.E()
            return None
        if mkey == 'W':
            self.W()
            return None
        raise ValueError(f'This method does not exist. : {mkey}')

    def S(self) -> None:
        tmp = [i for i in self.surface]
        self.surface[0] = tmp[4]
        self.surface[1] = tmp[0]
        self.surface[2] = tmp[2]
        self.surface[3] = tmp[3]
        self.surface[4] = tmp[5]
        self.surface[5] = tmp[1]

    def N(self) -> None:
        tmp = [i for i in self.surface]
        self.surface[0] = tmp[1]
        self.surface[1] = tmp[5]
        self.surface[2] = tmp[2]
        self.surface[3] = tmp[3]
        self.surface[4] = tmp[0]
        self.surface[5] = tmp[4]

    def E(self) -> None:
        tmp = [i for i in self.surface]
        self.surface[0] = tmp[3]
        self.surface[1] = tmp[1]
        self.surface[2] = tmp[0]
        self.surface[3] = tmp[5]
        self.surface[4] = tmp[4]
        self.surface[5] = tmp[2]

    def W(self) -> None:
        tmp = [i for i in self.surface]
        self.surface[0] = tmp[2]
        self.surface[1] = tmp[1]
        self.surface[2] = tmp[5]
        self.surface[3] = tmp[0]
        self.surface[4] = tmp[4]
        self.surface[5] = tmp[3]


# 提出用
data = [int(i) for i in input().split()]
order = list(input())

# # 動作確認用
# data = [int(i) for i in '1 2 4 8 16 32'.split()]
# order = list('EESWN')

dice = Dice(data)
for o in order:
    dice.invoke_method(o)
print(dice.get_upper_sursurface())

