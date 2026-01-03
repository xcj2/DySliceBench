import sys

import numpy as np


def input():
    return sys.stdin.readline()[:-1]


def ii(t: type = int):
    return t(input())


def il(t: type = int):
    return list(map(t, input().split()))


def imi(N: int, t: type = int):
    return [ii(t) for _ in range(N)]


def iml(N: int, t: type = int):
    return [il(t) for _ in range(N)]


def get_state(x, y):
    if x > y:
        return "Down"
    if x < y:
        return "Up"
    return "Equal"


N = ii()
A = il()
pre_state = None
c = 1
for i in range(N - 1):
    current_state = get_state(A[i], A[i + 1])
    if current_state == "Equal" or current_state == pre_state:
        continue
    if pre_state is None:
        pre_state = current_state
    else:
        pre_state = None
        c += 1
print(c)
