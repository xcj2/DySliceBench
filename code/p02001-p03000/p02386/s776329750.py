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


def isSameRollSide(d1, d2):
    if d1 == d2:
        return True
    rollDiceSide(d2)
    return False


def isSameRoll(d1, d2):
    if d1 == d2:
        return True
    rollDice(d2, "S")
    for _ in range(4):
        if isSameRollSide(d1, d2):
            return True
    return False


def isSameDice(d1, d2):
    for _ in range(4):
        for _ in range(4):
            if isSameRoll(d1, d2):
                return True
        rollDice(d2, "W")
    return False


n = int(input())
dice = [list(map(int, input().split())) for i in range(n)]
ans = [False for x in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if isSameDice(dice[i], dice[j]):
            ans[i] = True
            break
if True in ans:
    print("No")
else:
    print("Yes")

