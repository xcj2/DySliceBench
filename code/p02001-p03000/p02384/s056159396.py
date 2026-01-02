def main_1_11_A():
    values = list(map(int, input().split()))
    query = input()

    dice = Dice(values)
    for d in query:
        dice.roll(d)


def main_1_11_B():
    values = list(map(int, input().split()))
    n = int(input())

    for _ in range(n):
        t_value, s_value = map(int, input().split())

        print(_B(values, t_value, s_value))


def _B(values, t_value, s_value):
    """
    ????????¢?????????????????¨??????
    ??´??¢???????????¢?????????????????§???????????????????????¨?????????
    ??????????????????????????¢???????¢??????????
    """
    def rot_n(dice, n):
        for _ in range(n):
            dice.roll("N").roll("E").roll("S")
        return dice

    def make_dices():
        # ?????¢???TOP?????????
        return [
            Dice(values),
            Dice(values).roll("N"),
            Dice(values).roll("N").roll("N"),
            Dice(values).roll("N").roll("N").roll("N"),
            Dice(values).roll("E"),
            Dice(values).roll("W"),
        ]

    dices = (
        make_dices() +
        list(map(lambda dice: rot_n(dice, 1), make_dices())) +
        list(map(lambda dice: rot_n(dice, 2), make_dices())) +
        list(map(lambda dice: rot_n(dice, 3), make_dices()))
    )
    for dice in dices:
        # print(dice)
        for d in ("E" * 4 + "W" * 4 + "S" * 4 + "N" * 4):
            dice.roll(d)
            #print(d, (dice.top_value, dice.south_value), (t_value, s_value))
            if (dice.top_value, dice.south_value) == (t_value, s_value):
                return dice.east_value


class Dice:

    def __init__(self, values):
        self.values = values
        # top, bottom, direction 4
        self.t = 1
        self.b = 6
        self.w = 4
        self.e = 3
        self.n = 5
        self.s = 2

    def __repr__(self):
        labels = {
            "t": self.t,
            "b": self.b,
            "w": self.w,
            "e": self.e,
            "n": self.n,
            "s": self.s,
        }
        return "<%s (%s, %s)>" % (self.__class__, self.values, labels)

    def roll(self, direction):
        if direction == "E":
            after_lables = self.t, self.b, self.e, self.w
            self.e, self.w, self.b, self.t = after_lables
        elif direction == "W":
            after_lables = self.t, self.b, self.e, self.w
            self.w, self.e, self.t, self.b = after_lables
        elif direction == "S":
            after_lables = self.t, self.b, self.n, self.s
            self.s, self.n, self.t, self.b = after_lables
        elif direction == "N":
            after_lables = self.t, self.b, self.n, self.s
            self.n, self.s, self.b, self.t = after_lables

        return self

    @property
    def top_value(self):
        return self.values[self.t - 1]

    @property
    def south_value(self):
        return self.values[self.s - 1]

    @property
    def east_value(self):
        return self.values[self.e - 1]

if __name__ == "__main__":
    # main_1_11_A()
    main_1_11_B()