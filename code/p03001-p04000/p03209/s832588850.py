def patti(level):
    return 2 ** (level + 1) - 1


def burger(level):
    return 2 ** (level + 2) - 3


def get_ans(level, x, num_patti):
    if level == 0:
        return num_patti + x

    if x == 1 or x == 0:
        return num_patti
    elif x < 1 + burger(level - 1):
        x -= 1
        return get_ans(level - 1, x, num_patti)
    elif x == 1 + burger(level - 1):
        return patti(level - 1) + num_patti
    elif x == 1 + burger(level - 1) + 1:
        return patti(level - 1) + num_patti + 1
    elif x < 1 + burger(level - 1) + 1 + burger(level - 1):
        x -= 1 + burger(level - 1) + 1
        num_patti += 1 + patti(level - 1)
        tmp = get_ans(level - 1, x, num_patti)
        return tmp
    else:
        return num_patti + patti(level - 1) * 2 + 1


n, x = map(int, input().split())

print(get_ans(n, x, 0))