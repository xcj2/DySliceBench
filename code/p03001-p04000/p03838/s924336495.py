x, y = map(int, input().split())


def cal1(a, b):
    return print(b - a)


def cal2(a, b):
    return print(abs(a - b) + 2)


def cal3(a, b):
    return print(abs(abs(a) - abs(b)) + 1)


if x > 0 and y > 0:
    if x > y:
        cal2(x, y)
    else:
        cal1(x, y)

elif x < 0 and y < 0:
    if x > y:
        cal2(x, y)
    else:
        cal1(x, y)

elif x == 0:
    if y > 0:
        cal1(x, y)
    else:
        cal3(x, y)

elif y == 0:
    if x > 0:
        cal3(x, y)
    else:
        cal1(x, y)

elif x > 0 and y < 0:
    if abs(x) > abs(y):
        cal3(x, y)
    elif abs(x) < abs(y):
        cal3(x, y)
    else:
        print(1)

else:
    if abs(x) > abs(y):
        cal3(x, y)
    elif abs(x) < abs(y):
        cal3(x, y)
    else:
        print(1)