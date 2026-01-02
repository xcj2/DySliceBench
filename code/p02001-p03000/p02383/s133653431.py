from typing import List


class Dice:

    def __init__(self, s: List[int]):
        self.s = s

    def get_s(self) -> int:
        return self.s[0]

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

    def set_s(self, s0, s1, s2, s3, s4, s5) -> None:
        self.s[0] = s0
        self.s[1] = s1
        self.s[2] = s2
        self.s[3] = s3
        self.s[4] = s4
        self.s[5] = s5

    def S(self) -> None:
        self.set_s(self.s[4], self.s[0], self.s[2], self.s[3], self.s[5],
                   self.s[1])

    def N(self) -> None:
        self.set_s(self.s[1], self.s[5], self.s[2], self.s[3], self.s[0],
                   self.s[4])

    def E(self) -> None:
        self.set_s(self.s[3], self.s[1], self.s[0], self.s[5], self.s[4],
                   self.s[2])

    def W(self) -> None:
        self.set_s(self.s[2], self.s[1], self.s[5], self.s[0], self.s[4],
                   self.s[3])


# 提出用
data = [int(i) for i in input().split()]
order = list(input())

# # 動作確認用
# data = [int(i) for i in '1 2 4 8 16 32'.split()]
# order = list('SE')

dice = Dice(data)
for o in order:
    dice.invoke_method(o)
print(dice.get_s())

