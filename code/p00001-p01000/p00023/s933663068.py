# ??????????????¢??¨????????????, ????????¢???
def plus(a, b):
    return a + b


def minus(a, b):
    return abs(a - b)


def distance(x1, y1, x2, y2):
    r2 = (x1 - x2)**2 + (y1 - y2)**2
    return pow(r2, 0.5)


def flag(l):
    rp = plus(l[2], l[5])
    rm = minus(l[2], l[5])
    d = distance(l[0], l[1], l[3], l[4])
    if rp < d:
        return 0
    elif d < rm:
        if l[5] < l[2]:
            return 2
        else:
            return -2
    else:
        return 1


N = int(input())
for i in range(N):
    a = list(map(float, input().split()))
    print(flag(a))