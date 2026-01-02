# -*- coding: utf-8 -*-
from sys import stdin
# import numpy as np

s_in = lambda: stdin.readline()[:-1]  # s = s_in()
d_in = lambda: int(stdin.readline())  # N = d_in()
ds_in = lambda: list(map(int, stdin.readline().split()))  # List = ds_in()


N, Q = ds_in()
S = s_in()
move_list = []
for _ in range(Q):
    t, d = s_in().split()
    move_list.append([t, d])


def disappear(place, array):
    if place == -1:
        return (False, False)
    else:
        left = False
        right = False
        for i in range(Q):
            current_char = array[place]
            t, d = move_list[i]
            if t == current_char:
                if d == 'R':
                    place += 1
                else:
                    place -= 1
                if place < 0:
                    left = True
                    break
                elif place > N-1:
                    right = True
                    break
        return (left, right)


def bisect_left(array):
    start, end = -1, N
    while end - start > 1:
        t = start + (end-start)//2
        if disappear(t, array)[0]:
            start = t
        else:
            end = t
    return start


def bisect_right(array):
    start, end = -1, N
    while end - start > 1:
        t = start + (end-start)//2
        if disappear(t, array)[1]:
            end = t
        else:
            start = t
    return start


list_s = list(S)
left = bisect_left(list_s)
right = bisect_right(list_s)
print(right - left)
