import numpy as np


card = np.array([list(map(int, input().split())) for _ in range(3)], dtype=np.int64)
n = int(input())
for _ in range(n):
    num = int(input())
    card[card == num] = 0
card = card == 0


def check_vertical(card):
    return np.all(card, axis=0).sum() >= 1


def check_horizon(card):
    return np.all(card, axis=1).sum() >= 1


def check_diagonal(card):
    check1 = np.diag(card).sum()
    check2 = np.diag(np.fliplr(card)).sum()
    return check1 == 3 or check2 == 3


if check_vertical(card) or check_horizon(card) or check_diagonal(card):
    print('Yes')
else:
    print('No')
