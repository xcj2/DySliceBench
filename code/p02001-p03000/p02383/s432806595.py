from typing import List


class Dice():
    def __init__(self, lst):
        self.top = lst[0]
        self.front = lst[1]
        self.right = lst[2]
        self.left = lst[3]
        self.back = lst[4]
        self.bottom = lst[5]

    def rotate(self, direction):
        if direction == "E":
            self.top, self.right, self.bottom, self.left = self.left, self.top, self.right, self.bottom
        if direction == "N":
            self.top, self.back, self.bottom, self.front = self.front, self.top, self.back, self.bottom
        if direction == "S":
            self.top, self.front, self.bottom, self.back = self.back, self.top, self.front, self.bottom
        if direction == "W":
            self.top, self.left, self.bottom, self.right = self.right, self.top, self.left, self.bottom


def main():
    dice_nums: List[int] = list(map(int, input().split()))
    directions: str = input()

    dice = Dice(dice_nums)
    for direction in directions:
        dice.rotate(direction)
    print(dice.top)


if __name__ == "__main__":
    main()

