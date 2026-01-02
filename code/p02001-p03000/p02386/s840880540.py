ROLL_MASTER = (
    (0, 1, 2, 3, 4, 5), (1, 0, 3, 2, 5, 4), (2, 0, 1, 4, 5, 3),
    (3, 0, 4, 1, 5, 2), (4, 0, 2, 3, 5, 1), (5, 1, 3, 2, 4, 0))
TWIST_MASTER = (0, 2, 4, 1, 3, 5)


def roll(dice, top):
    return tuple(dice[i] for i in ROLL_MASTER[top])


def twist(dice):
    return tuple(dice[i] for i in TWIST_MASTER)


def twist_check(d1, d2):
    if d1[0] != d2[0] or d1[5] != d2[5]:
        return False
    for _ in range(4):
        if d1 == d2:
            return True
        d2 = twist(d2)
    return False


def equal_check(d1, d2):
    for i in range(6):
        if twist_check(d1, roll(d2, i)):
            return True
    return False


def differs_all():
    n, d1, dset = int(input()), tuple(map(int, input().split())), set()
    dset.add(d1)

    for _ in range(n - 1):
        d2 = tuple(map(int, input().split()))
        for d1 in dset:
            if equal_check(d1, d2):
                return False
        dset.add(d2)
    return True


print('Yes' if differs_all() else 'No')