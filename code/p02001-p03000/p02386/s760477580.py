import sys
import os


N = int(input())
dices = []
for i in range(N):
    dice = list(map(int, input().split()))
    dices.append(dice)

def dice_roll(dice, c):
    copy = dice[:]
    if c == 'E':
        dice[2] = copy[0]
        dice[5] = copy[2]
        dice[3] = copy[5]
        dice[0] = copy[3]
    elif c == 'N':
        dice[0] = copy[1]
        dice[4] = copy[0]
        dice[5] = copy[4]
        dice[1] = copy[5]
        pass
    elif c == 'S':
        dice[1] = copy[0]
        dice[0] = copy[4]
        dice[4] = copy[5]
        dice[5] = copy[1]
    elif c == 'W':
        dice[0] = copy[2]
        dice[2] = copy[5]
        dice[5] = copy[3]
        dice[3] = copy[0]
    # Y???????????¢
    elif c == 'R':
        dice[2] = copy[1]
        dice[4] = copy[2]
        dice[3] = copy[4]
        dice[1] = copy[3]
    return dice


def check(dice0_input, dice1_input):
    # ??????????????¶?????????????????????????????????copy?????±???
    dice0 = dice0_input[:]
    dice1 = dice1_input[:]

    # up???????????????
    num = 0
    while dice0[0] != dice1[0]:
        if num % 2 == 0:
            dice0 = dice_roll(dice0, 'E')
        else:
            dice0 = dice_roll(dice0, 'N')
        num += 1
        if num > 10:
            return False

    # front???????????????
    num = 0
    while dice0[1] != dice1[1]:
        dice0 = dice_roll(dice0, 'R')
        num += 1
        if num > 10:
            return False

    if dice0[2] == dice1[2] and dice0[3] == dice1[3] and dice0[4] == dice1[4] and dice0[5] == dice1[5]:
        return True
    else:
        return False


def check2(dice0, dice1):
    # ?????¨????????¢???????????????6????????§????????????
    for i in range(6):
        result = check(dice0, dice1)
        if result:
            return True
        else:
            if i % 2 == 0:
                dice0 = dice_roll(dice0, 'N')
            else:
                dice0 = dice_roll(dice0, 'E')
    return False

for i in range(N):
    for j in range(i+1, N):
        is_same = check2(dices[i], dices[j])
        if is_same:
            print('No')
            quit()
print('Yes')
