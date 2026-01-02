class Dice(object):
    def __init__(self, init_numbers: list):
        self.numbers = dict(zip(("T", "S", "E", "W", "N", "B"), init_numbers))

    def _roll(self, old_part: tuple):
        new_part = old_part[1:] + (old_part[0],)
        new_numbers = [self.numbers[face] for face in new_part]

        for old, new in zip(old_part, new_numbers):
            self.numbers[old] = new

    def vroll(self, reverse=False):
        """北方向に回転"""
        old_part = ("N", "T", "S", "B")
        self._roll(old_part if not reverse else old_part[::-1])

    def hroll(self, reverse=False):
        """時計回りに回転"""
        old_part = ("N", "W", "S", "E")
        self._roll(old_part if not reverse else old_part[::-1])

    def roll_to(self, direction: str):

        if direction == "N":
            self.vroll()
        elif direction == "S":
            self.vroll(reverse=True)
        elif direction == "E":
            self.hroll(reverse=True)
            self.vroll()
            self.hroll()
        elif direction == "W":
            self.hroll()
            self.vroll()
            self.hroll(reverse=True)
        else:
            raise AssertionError


def is_same(dice1: Dice, dice2: Dice):

    result = False

    for direction in ["N", "E"] * 3:
        dice1.roll_to(direction)
        for _ in range(4):
            result |= dice1.numbers == dice2.numbers
            dice1.hroll()

    return result


if __name__ == "__main__":
    from itertools import combinations

    n = int(input())
    dices = []
    for _ in range(n):
        dices.append(Dice(list(map(int, input().split()))))

    all_different = True
    for i, j in combinations(dices, r=2):
        all_different &= not is_same(i, j)

    print("Yes" if all_different else "No")

