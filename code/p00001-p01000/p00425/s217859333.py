dice = [0,1,2,3,4,5,6]


def north():
    ret = [0]
    global dice
    ret.append(dice[2])
    ret.append(dice[6])
    ret.append(dice[3])
    ret.append(dice[4])
    ret.append(dice[1])
    ret.append(dice[5])

    dice = ret.copy()


def east():
    ret = [0]
    global dice
    ret.append(dice[4])
    ret.append(dice[2])
    ret.append(dice[1])
    ret.append(dice[6])
    ret.append(dice[5])
    ret.append(dice[3])

    dice = ret.copy()


def west():
    ret = [0]
    global dice
    ret.append(dice[3])
    ret.append(dice[2])
    ret.append(dice[6])
    ret.append(dice[1])
    ret.append(dice[5])
    ret.append(dice[4])

    dice = ret.copy()


def south():
    ret = [0]
    global dice
    ret.append(dice[5])
    ret.append(dice[1])
    ret.append(dice[3])
    ret.append(dice[4])
    ret.append(dice[6])
    ret.append(dice[2])

    dice = ret.copy()


def right():
    ret = [0]
    global dice
    ret.append(dice[1])
    ret.append(dice[3])
    ret.append(dice[5])
    ret.append(dice[2])
    ret.append(dice[4])
    ret.append(dice[6])

    dice = ret.copy()

def left():
    ret = [0]
    global dice
    ret.append(dice[1])
    ret.append(dice[4])
    ret.append(dice[2])
    ret.append(dice[5])
    ret.append(dice[3])
    ret.append(dice[6])

    dice = ret.copy()

total_score = 1

while True:
    n = int(input())
    if n == 0:
        break

    for i in range(n):
        input_str = input()

        if input_str == 'North':
            north()
        elif input_str == 'East':
            east()
        elif input_str == 'West':
            west()
        elif input_str == 'South':
            south()
        elif input_str == 'Right':
            right()
        else:
            left()
        total_score += dice[1]

    print(total_score)
    total_score = 1
    dice = [i for i in range(0, 7)]

