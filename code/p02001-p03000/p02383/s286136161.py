import copy


class Dice:
    def __init__(self, eyes: [int]):
        self.__eyes = eyes

    def top(self):
        return self.__eyes[0]

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

    def roll_n(self):
        tmp = copy.copy(self.__eyes)
        tmp[0] = self.__eyes[1]
        tmp[1] = self.__eyes[5]
        tmp[2] = self.__eyes[2]
        tmp[3] = self.__eyes[3]
        tmp[4] = self.__eyes[0]
        tmp[5] = self.__eyes[4]
        self.__eyes = tmp

    def roll_w(self):
        tmp = copy.copy(self.__eyes)
        tmp[0] = self.__eyes[2]
        tmp[1] = self.__eyes[1]
        tmp[2] = self.__eyes[5]
        tmp[3] = self.__eyes[0]
        tmp[4] = self.__eyes[4]
        tmp[5] = self.__eyes[3]
        self.__eyes = tmp

    def roll(self, direction: str):
        if direction == 'N':
            self.roll_n()
        if direction == 'E':
            self.roll_e()
        if direction == 'S':
            self.roll_s()
        if direction == 'W':
            self.roll_w()


def resolve():
    eyes = list(map(int, input().split()))
    directions = list(input())
    dice = Dice(eyes)
    for direction in directions:
        dice.roll(direction)
    print(dice.top())


resolve()

