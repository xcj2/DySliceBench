def North(dice):
    w = dice[0]
    dice[0] = dice[1]
    dice[1] = dice[5]
    dice[5] = dice[4]
    dice[4] = w
    return dice
def East(dice):
    w = Dice[0]
    dice[0] = dice[3]
    dice[3] = dice[5]
    dice[5] = dice[2]
    dice[2] = w
    return dice
def South(dice):
    w = dice[0]
    dice[0] = dice[4]
    dice[4] = dice[5]
    dice[5] = dice[1]
    dice[1] = w
    return dice
def West(dice):
    w = dice[0]
    dice[0] = dice[2]
    dice[2] = dice[5]
    dice[5] = dice[3]
    dice[3] = w
    return dice

Dice = input().split()
Roll = list(input())

for roll in Roll:
    if roll == 'N':
        Dice = North(Dice)
        continue
    if roll == 'E':
        Dice = East(Dice)
        continue
    if roll == 'S':
        Dice = South(Dice)
        continue
    if roll == 'W':
        Dice = West(Dice)
        continue

print(Dice[0])