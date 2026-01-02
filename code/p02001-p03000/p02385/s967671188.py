import random

dice_a = list(map(int, input().split()))
dice_b = list(map(int, input().split()))


class Dice():
    def __init__(self, dice, directions):
        self.dice = dice
        self.directions = directions

    def roll(self):
        for direction in self.directions:
            NS = [0, 1, 5, 4]
            WE = [0, 2, 5, 3]
            copy_dice = self.dice[:]

            if direction == 'N':
                for j in range(4):
                    self.dice[NS[j]] = copy_dice[NS[j-3]]
            elif direction == 'S':
                for j in range(4):
                    self.dice[NS[j]] = copy_dice[NS[j-1]]
            elif direction == 'W':
                for j in range(4):
                    self.dice[WE[j]] = copy_dice[WE[j-3]]
            else:
                for j in range(4):
                    self.dice[WE[j]] = copy_dice[WE[j-1]]

        return self.dice


def check_equal(dice_1, dice_2):
    for i in range(777):
        dice_A = Dice(dice_1, random.choice(['N', 'S', 'W', 'E']))

        if dice_A.roll() == dice_2:
            print('Yes')
            break

    else:
        print('No')

check_equal(dice_a, dice_b)
