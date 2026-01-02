import copy


class Dice:
    def __init__(self, eyes: [int]):
        self.__eyes = eyes

    @property
    def eyes(self):
        return self.__eyes

    def top(self):
        return self.__eyes[0]

    def right(self):  # pragma no cover
        return self.__eyes[2]

    def roll_s(self):
        tmp = copy.copy(self.__eyes)
        tmp[0] = self.__eyes[4]
        tmp[1] = self.__eyes[0]
        tmp[2] = self.__eyes[2]
        tmp[3] = self.__eyes[3]
        tmp[4] = self.__eyes[5]
        tmp[5] = self.__eyes[1]
        self.__eyes = tmp

    def roll_e(self):
        tmp = copy.copy(self.__eyes)
        tmp[0] = self.__eyes[3]
        tmp[1] = self.__eyes[1]
        tmp[2] = self.__eyes[0]
        tmp[3] = self.__eyes[5]
        tmp[4] = self.__eyes[4]
        tmp[5] = self.__eyes[2]
        self.__eyes = tmp

    def roll_n(self):  # pragma no cover
        tmp = copy.copy(self.__eyes)
        tmp[0] = self.__eyes[1]
        tmp[1] = self.__eyes[5]
        tmp[2] = self.__eyes[2]
        tmp[3] = self.__eyes[3]
        tmp[4] = self.__eyes[0]
        tmp[5] = self.__eyes[4]
        self.__eyes = tmp

    def roll_w(self):  # pragma no cover
        tmp = copy.copy(self.__eyes)
        tmp[0] = self.__eyes[2]
        tmp[1] = self.__eyes[1]
        tmp[2] = self.__eyes[5]
        tmp[3] = self.__eyes[0]
        tmp[4] = self.__eyes[4]
        tmp[5] = self.__eyes[3]
        self.__eyes = tmp

    def turn_right(self):
        tmp = copy.copy(self.__eyes)
        tmp[0] = self.__eyes[0]
        tmp[1] = self.__eyes[3]
        tmp[2] = self.__eyes[1]
        tmp[3] = self.__eyes[4]
        tmp[4] = self.__eyes[2]
        tmp[5] = self.__eyes[5]
        self.__eyes = tmp

    def front(self):
        return self.__eyes[1]

    def roll(self, direction: str):  # pragma no cover
        if direction.lower() == 'n':
            self.roll_n()
        if direction.lower() == 'e':
            self.roll_e()
        if direction.lower() == 's':
            self.roll_s()
        if direction.lower() == 'w':
            self.roll_w()

    def __eq__(self, other):
        # 全出目を比較する
        is_same = False
        for _ in range(2):
            for _ in range(3):
                for _ in range(4):
                    if self.eyes == other.eyes:
                        is_same = True
                    self.turn_right()
                self.roll_n()
            self.turn_right()
            self.roll_s()
        return is_same


def resolve():
    n = int(input())
    dices = []

    for _ in range(n):
        eyes = list(map(int, input().split()))
        dices.append(Dice(eyes))

    found = False
    while len(dices) > 0:
        dice = dices.pop(0)
        for d in dices:
            if dice == d:
                found = True

    if found:
        print("No")
    else:
        print("Yes")


resolve()

