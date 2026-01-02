def east(dice):
    buff = [d for d in dice]
    dice[0] = buff[3]
    dice[2] = buff[0]
    dice[5] = buff[2]
    dice[3] = buff[5]


def west(dice):
    buff = [d for d in dice]
    dice[0] = buff[2]
    dice[2] = buff[5]
    dice[5] = buff[3]
    dice[3] = buff[0]


def north(dice):
    buff = [d for d in dice]
    dice[0] = buff[1]
    dice[1] = buff[5]
    dice[5] = buff[4]
    dice[4] = buff[0]


def south(dice):
    buff = [d for d in dice]
    dice[0] = buff[4]
    dice[1] = buff[0]
    dice[5] = buff[1]
    dice[4] = buff[5]


dice = list(map(int, input().split()))
commands = input()

for c in commands:
    if c == "E":
        east(dice)
    elif c == "W":
        west(dice)
    elif c == "N":
        north(dice)
    elif c == "S":
        south(dice)
    else:
        break

print(dice[0])