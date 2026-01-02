import copy


class Dice:
    def __init__(self, one: int, two: int, three: int, four: int, five: int, six: int) -> None:
        self.__one = one
        self.__two = two
        self.__three = three
        self.__four = four
        self.__five = five
        self.__six = six

    def roll(self, direction) -> None:
        if direction == "N":
            tmp = self.__one
            self.__one = self.__two
            self.__two = self.__six
            self.__six = self.__five
            self.__five = tmp

        if direction == "E":
            tmp = self.__one
            self.__one = self.__four
            self.__four = self.__six
            self.__six = self.__three
            self.__three = tmp

        if direction == "S":
            tmp = self.__one
            self.__one = self.__five
            self.__five = self.__six
            self.__six = self.__two
            self.__two = tmp

        if direction == "W":
            tmp = self.__one
            self.__one = self.__three
            self.__three = self.__six
            self.__six = self.__four
            self.__four = tmp

        if direction == "I":
            tmp = self.__one
            self.__one, self.__six = self.__six, self.__one
            self.__two, self.__five = self.__five, self.__two

    def set_top(self, top: int) -> bool:
        if self.__one != top:
            for i in range(3):
                self.roll("N")
                if (self.__one == top):
                    break
        if self.__one != top:
            for i in range(3):
                self.roll("E")
                if (self.__one == top):
                    break
        return self.__one == top

    def rotate(self) -> None:
        tmp = self.__two
        self.__two = self.__four
        self.__four = self.__five
        self.__five = self.__three
        self.__three = tmp

    def check(self, dice) -> bool:
        flag = True
        if self.__one != dice.__one:
            flag = False
        if self.__two != dice.__two:
            flag = False
        if self.__three != dice.__three:
            flag = False
        if self.__four != dice.__four:
            flag = False
        if self.__five != dice.__five:
            flag = False
        if self.__six != dice.__six:
            flag = False
        return flag

    @property
    def top(self) -> int:
        return self.__one

    @property
    def front(self) -> int:
        return self.__two

    @property
    def right(self) -> int:
        return self.__three

    @property
    def left(self) -> int:
        return self.__four

    @property
    def back(self) -> int:
        return self.__five

    @property
    def bottom(self) -> int:
        return self.__six


if __name__ == "__main__":
    dice1_one, dice1_two, dice1_three, dice1_four, dice1_five, dice1_six = map(
        int, input().split(' '))
    dice2_one, dice2_two, dice2_three, dice2_four, dice2_five, dice2_six = map(
        int, input().split(' '))

    dice1 = Dice(dice1_one, dice1_two, dice1_three,
                 dice1_four, dice1_five, dice1_six)
    dice2 = Dice(dice2_one, dice2_two, dice2_three,
                 dice2_four, dice2_five, dice2_six)

    directions = ["N", "E", "S", "W", "I"]
    for direction in directions:
        dice = copy.deepcopy(dice1)
        if not (dice1.top == dice2.top and dice1.bottom == dice2.bottom):
            dice.roll(direction)
        if dice.top == dice2.top and dice.bottom == dice2.bottom:
            if dice.front != dice2.front:
                for i in range(3):
                    dice.rotate()
                    if dice.check(dice2):
                        print("Yes")
                        exit()
            else:
                if dice.check(dice2):
                    print("Yes")
                    exit()
    print("No")

