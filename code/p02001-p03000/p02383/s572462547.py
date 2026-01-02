# Dice I
class Dice:
    def __init__(self, default_surface):
        self.dice = default_surface  # [T, B, U, D, L, R]
        self.rotation_count = 0

    def move(self, new_face: int) -> None:
        for i, face in enumerate(self.dice):  # move new_face to dice[0]
            if face != new_face:
                continue
            elif i == 1:
                self.roll_up(), self.roll_up()
            elif i == 2:
                self.roll_left()
            elif i == 3:
                self.roll_right()
            elif i == 4:
                self.roll_up()
            elif i == 5:
                self.roll_down()

    def roll_left(self) -> None:
        self.dice[0], self.dice[3], self.dice[1], self.dice[2] = self.dice[2], self.dice[0], self.dice[3], self.dice[1]
        self.rotation_count += 1

    def roll_right(self) -> None:
        self.dice[0], self.dice[2], self.dice[1], self.dice[3] = self.dice[3], self.dice[0], self.dice[2], self.dice[1]
        self.rotation_count += 1

    def roll_up(self) -> None:
        self.dice[0], self.dice[5], self.dice[1], self.dice[4] = self.dice[4], self.dice[0], self.dice[5], self.dice[1]
        self.rotation_count += 1

    def roll_down(self) -> None:
        self.dice[0], self.dice[4], self.dice[1], self.dice[5] = self.dice[5], self.dice[0], self.dice[4], self.dice[1]
        self.rotation_count += 1

    def roll_clockwise(self) -> None:
        self.dice[2], self.dice[4], self.dice[3], self.dice[5] = self.dice[5], self.dice[2], self.dice[4], self.dice[3]
        self.rotation_count += 1

    def roll_counterclockwise(self) -> None:
        self.dice[2], self.dice[5], self.dice[3], self.dice[4] = self.dice[4], self.dice[2], self.dice[5], self.dice[3]
        self.rotation_count += 1


def main():
    T, L, U, D, R, B = map(int, input().split())
    order = input().rstrip()
    dice = Dice([T, B, U, D, L, R])
    for c in order:
        if c == "E":
            dice.roll_right()
        if c == "W":
            dice.roll_left()
        if c == "N":
            dice.roll_up()
        if c == "S":
            dice.roll_down()
    print(dice.dice[0])


if __name__ == "__main__":
    main()

