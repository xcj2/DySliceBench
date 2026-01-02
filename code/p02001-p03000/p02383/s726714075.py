def main():
    values = list(map(int, input().split()))
    query = input()

    dice = Dice(values)
    for d in query:
        dice.roll(d)

    print(dice.top_value)


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

    @property
    def top_value(self):
        return self.values[self.t - 1]

if __name__ == "__main__":
    main()