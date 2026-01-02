def roll_e(d):
    w = []
    w = d
    d[0], d[1], d[2], d[3], d[4], d[5] = w[3], w[1], w[0], w[5], w[4], w[2]
    return d

def roll_s(d):
    w = []
    w = d
    d[0], d[1], d[2], d[3], d[4], d[5] = w[4], w[0], w[2], w[3], w[5], w[1]
    return d

def dice_judge(d1, d2):
    no_flag = 0

    i = 0
    while d1[1] != d2[1]:
        if i == 7:
            no_flag = 1
            break
        elif i == 4:
            d2 = roll_e(d2)
        d2 = roll_s(d2)
        i += 1

    i = 0
    while d1[0] != d2[0] and no_flag == 0:
        if i == 4:
            break
        d2 = roll_e(d2)
        i += 1

    if d1 == d2:
        return True
    else:
        return False

n = int(input())
d = []
no_flag = 0

i = 0
while n > i:
    d.append(input().split())
    i += 1
i, j = 0, 0
while n-1 > i:
    j = i + 1
    while n > j:
        if dice_judge(d[i], d[j]):
            no_flag = 1
        j += 1
    i += 1

if no_flag == 0:
    print("Yes")
elif no_flag == 1:
    print("No")

