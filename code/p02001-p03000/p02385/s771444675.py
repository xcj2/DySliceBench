import sys


def rollDice(dice, direction):
    buf = [x for x in dice]
    if direction == "S":
        buf[0] = dice[4]
        buf[1] = dice[0]
        buf[4] = dice[5]
        buf[5] = dice[1]
    elif direction == "E":
        buf[0] = dice[3]
        buf[2] = dice[0]
        buf[3] = dice[5]
        buf[5] = dice[2]
    elif direction == "W":
        buf[0] = dice[2]
        buf[2] = dice[5]
        buf[3] = dice[0]
        buf[5] = dice[3]
    elif direction == "N":
        buf[0] = dice[1]
        buf[1] = dice[5]
        buf[4] = dice[0]
        buf[5] = dice[4]

    for i in range(6):
        dice[i] = buf[i]


def rollDiceSide(dice):
    buf = [x for x in dice]
    buf[1] = dice[2]
    buf[2] = dice[4]
    buf[3] = dice[1]
    buf[4] = dice[3]

    for i in range(6):
        dice[i] = buf[i]


def rollCheckSide(d):
    if d1 == d2:
        print("Yes")
        sys.exit()
    rollDiceSide(d2)


def rollCheck(d):
    if d1 == d2:
        print("Yes")
        sys.exit()
    rollDice(d2, "S")
    for _ in range(4):
        rollCheckSide(d2)


d1 = list(map(int, input().split()))
d2 = list(map(int, input().split()))


for _ in range(4):
    for _ in range(4):
        rollCheck(d2)
    rollDice(d2, "W")

print("No")

