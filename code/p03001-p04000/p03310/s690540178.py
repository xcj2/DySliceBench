# -*- coding: utf-8 -*-
from sys import stdin
import numpy as np

d_in = lambda: int(stdin.readline())  # N = d_in()
ds_in = lambda: list(map(int, stdin.readline().split()))  # List = ds_in()


def left_diff(array):
    """
    array: ordered ndarray, len(array) >= 2
    """
    x = (array[-1] + 1) >> 1
    mid = np.searchsorted(array, x)
    if abs(array[-1] - array[mid] * 2) < abs(array[-1] - array[mid-1] * 2):
        return array[mid], array[-1] - array[mid]
    else:
        return array[mid-1], array[-1] - array[mid-1]


def right_diff(array, offset):
    """
    array: ordered ndarray, len(array) >= 2
        target array or list

    offset: int
        offset value for right array
    """
    x = (array[-1] - offset + 1) >> 1
    mid = np.searchsorted(array, x + offset)
    if abs(array[-1] - array[mid] * 2 + offset)\
            < abs(array[-1] - array[mid-1] * 2 + offset):
        return array[mid] - offset, array[-1] - array[mid]
    else:
        return array[mid-1] - offset, array[-1] - array[mid-1]


def calc_max_diff(p, q, r, s):
    return max(p, q, r, s) - min(p, q, r, s)


if __name__ == '__main__':
    N = d_in()
    a_array = np.array(ds_in())

    cum_a = np.cumsum(a_array)
    left_cut_points = (cum_a[1:-2] + 1) // 2
    left_mid_points = np.searchsorted(cum_a, left_cut_points)
    right_cut_points = (cum_a[-1] + cum_a[1:-2] + 1) // 2
    right_mid_points = np.searchsorted(cum_a, right_cut_points)
    
    ans = float('inf')
    for i in range(2):
        for j in range(2):
            P = cum_a[left_mid_points-i]
            Q = cum_a[1:-2] - P
            R = cum_a[right_mid_points-j] - cum_a[1:-2]
            S = cum_a[-1] - cum_a[right_mid_points-j]
            MAX = np.maximum(np.maximum(P, Q), np.maximum(R, S))
            MIN = np.minimum(np.minimum(P, Q), np.minimum(R, S))
            ans = min(ans, (MAX - MIN).min())

    print(ans)
