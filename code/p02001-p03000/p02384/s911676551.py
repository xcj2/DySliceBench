class Dice:
    def __init__(self, top: str, front: str, right: str, left: str, back: str, bottom: str) -> None:
        self.top = top
        self.front = front
        self.right = right
        self.left = left
        self.back = back
        self.bottom = bottom

    def print_top(self):
        print(self.top)

    def print_right(self):
        print(self.right)

    def roll(self, direction: str) -> None:
        if direction == 'S':
            self.south()
        elif direction == 'N':
            self.north()
        elif direction == 'E':
            self.east()
        elif direction == 'W':
            self.west()

    def north(self):
        [self.top, self.back, self.bottom, self.front] = [self.front, self.top, self.back, self.bottom]

    def south(self):
        [self.top, self.back, self.bottom, self.front] = [self.back, self.bottom, self.front, self.top]

    def east(self):
        [self.top, self.right, self.bottom, self.left] = [self.left, self.top, self.right, self.bottom]

    def west(self):
        [self.top, self.right, self.bottom, self.left] = [self.right, self.bottom, self.left, self.top]

    def rotate_right(self) -> None:
        for direction in 'SWN':
            dice.roll(direction)


def solve(dice: Dice, top: str, front: str) -> None:
    # find top
    found = False
    for direction in 'SSSS':
        dice.roll(direction)
        if dice.top == top:
            found = True
            break
    if not found:
        for direction in 'EEE':
            dice.roll(direction)
            if dice.top == top:
                break

    # find front
    for _ in range(4):
        dice.rotate_right()
        if dice.front == front:
            break

    # answer right
    dice.print_right()


labels = input().split()
dice = Dice(*labels)
n = int(input())
for i in range(n):
    top, front = input().split()
    solve(dice, top, front)

