# Dice I
# 2018/11/17

class Dice:
    def __init__(self, *num):
        if len(num) != 6:
            raise ValueError("6!")
        self.numbers = num

    def east(self):
        index = (3, 1, 0, 5, 4, 2)
        self.numbers = tuple((self.numbers[i] for i in index))

    def west(self):
        index = (2, 1, 5, 0, 4, 3)
        self.numbers = tuple((self.numbers[i] for i in index))

    def south(self):
        index = (4, 0, 2, 3, 5, 1)
        self.numbers = tuple((self.numbers[i] for i in index))

    def north(self):
        index = (1, 5, 2, 3, 0, 4)
        self.numbers = tuple((self.numbers[i] for i in index))

    @property
    def top(self):
        return self.numbers[0]

    def __repr__(self):
        return "Dice(" + ", ".join([str(i) for i in self.numbers]) + ")"


def main():
    num = [int(i) for i in input().rstrip().split()]
    dice = Dice(*num)
    for i in input().rstrip():
        if i == "E":
            dice.east()
        elif i == "W":
            dice.west()
        elif i == "S":
            dice.south()
        elif i == "N":
            dice.north()
    print(dice.top)

if __name__ == "__main__":
    main()
