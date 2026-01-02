class Dice(object):
    def __init__(self, faces):
        self.top = faces[0]
        self.south = faces[1]
        self.east = faces[2]
        self.west = faces[3]
        self.north = faces[4]
        self.bottom = faces[5]

    def rotate(self, command):
        pre_top = self.top
        if command == 'N':
            self.top = self.south
            self.south = self.bottom
            self.bottom = self.north
            self.north = pre_top
        elif command == 'E':
            self.top = self.west
            self.west = self.bottom
            self.bottom = self.east
            self.east = pre_top
        elif command == 'W':
            self.top = self.east
            self.east = self.bottom
            self.bottom = self.west
            self.west = pre_top
        elif command == 'S':
            self.top = self.north
            self.north = self.bottom
            self.bottom = self.south
            self.south = pre_top


def main() -> None:
    *dice_values, = map(int, input().split())
    dice_x = Dice(dice_values)

    commands = input()
    for command in commands:
        dice_x.rotate(command)

    print(dice_x.top)


if __name__ == '__main__':
    main()
