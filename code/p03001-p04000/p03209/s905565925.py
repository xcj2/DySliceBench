n, x = map(int, input().split())


def p(level):
    if level == 0:
        return 1
    return 2*p(level-1)+1


def a(level):
    if level == 0:
        return 1
    return 2*a(level-1)+3


def f(level, x):
    if level == 0:
        return 1
    elif x == 1:
        return 0
    else:
        if 1 < x <= 1 + a(level-1):
            return f(level-1, x-1)
        else:
            if x == 2 + a(level-1):
                return 1 + p(level-1)
            elif 2+a(level-1) < x <= 2 + 2*a(level-1):
                return 1 + p(level-1)+f(level-1, x-2-a(level-1))
            elif x == 3 + 2*a(level-1):
                return 1 + 2*p(level-1)


print(f(n, x))