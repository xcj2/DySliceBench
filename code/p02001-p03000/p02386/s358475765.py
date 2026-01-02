import random

n = int(input())
dice_list = [list(map(int, input().split())) for i in range(n)]


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
    for i in range(n+100):
        dice_A = Dice(dice_1, random.choice(['N', 'S', 'W', 'E']))

        if dice_A.roll() == dice_2:
            return True
            break

    else:
        return False

check_dice = True

for i in range(n):
    for j in range(i+1, n):
        if check_equal(dice_list[i], dice_list[j]) == True:
            check_dice = False
            break


if check_dice == True:
    print('Yes')
else:
    print('No')
