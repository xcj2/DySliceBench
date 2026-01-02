#!usr/bin/env python3

import sys


class Die:
    def __init__(self, pips):
        self.pips = pips

    def move_die(self, direction):
        tmp = int()
        if direction == 'N':
            tmp = self.pips[0]
            self.pips[0] = self.pips[1]
            self.pips[1] = self.pips[5]
            self.pips[5] = self.pips[4]
            self.pips[4] = tmp
        elif direction == 'S':
            tmp = self.pips[0]
            self.pips[0] = self.pips[4]
            self.pips[4] = self.pips[5]
            self.pips[5] = self.pips[1]
            self.pips[1] = tmp
        elif direction == 'E':
            tmp = self.pips[0]
            self.pips[0] = self.pips[3]
            self.pips[3] = self.pips[5]
            self.pips[5] = self.pips[2]
            self.pips[2] = tmp
        elif direction == 'W':
            tmp = self.pips[0]
            self.pips[0] = self.pips[2]
            self.pips[2] = self.pips[5]
            self.pips[5] = self.pips[3]
            self.pips[3] = tmp

    def print_upside(self):
        print(self.pips[0])


def main():
    pips = [int(pip) for pip in sys.stdin.readline().strip('\n').split()]
    die = Die(pips)
    directions = list(sys.stdin.readline().strip('\n'))

    for direction in directions:
        die.move_die(direction)

    die.print_upside()


if __name__ == '__main__':
    main()