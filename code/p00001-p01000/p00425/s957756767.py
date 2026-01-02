def North(d):
    d[0], d[1], d[3], d[5] = d[1], d[5], d[0], d[3]
    return int(d[0])

def West(d):
    d[0], d[2], d[4], d[5] = d[2], d[5], d[0], d[4]
    return int(d[0])

def East(d):
    d[0], d[2], d[4], d[5] = d[4], d[0], d[5], d[2]
    return int(d[0])

def South(d):
    d[0], d[1], d[3], d[5] = d[3], d[0], d[5], d[1]
    return int(d[0])

def Right(d):
    d[1], d[2], d[3], d[4] = d[2], d[3], d[4], d[1]
    return int(d[0])

def Left(d):
    d[1], d[2], d[3], d[4] = d[4], d[1], d[2], d[3]
    return int(d[0])

while True:
    n = int(input())
    if n == 0:
        break

    dice = ['1','2','3','5','4','6']
    total = 1
    for i in range(n):
        ss = str(input().split()[0])
        if ss == "North":
            total += North(dice)

        elif ss == "West":
            total += West(dice)

        elif ss == "East":
            total += East(dice)

        elif ss == "South":
            total += South(dice)

        elif ss == "Right":
            total += Right(dice)

        elif ss == "Left":
            total += Left(dice)
    print(total)