# -*- coding: utf-8 -*-

import sys
import os
import math

H, W = map(int, input().split())

def vertical_cut(H, W):
    if W < 3:
        return float('inf')

    if W % 3 == 0:
        min_w = W // 3
        max_w = W // 3
    else:
        min_w = W // 3
        max_w = W // 3 + 1

    S_max = max_w * H
    S_min = min_w * H

    return S_max - S_min

def horizontal_cut(H, W):
    return vertical_cut(W, H)

def vertical_and_horizontal_cut(H, W):
    min_score = float('inf')

    for cut_i in range(1, W // 2 + 1):
        left_S = cut_i * H
        right_W = W - cut_i

        right_H_top = H // 2
        right_H_bottom = H - right_H_top

        right_top_S = right_W * right_H_top
        right_bottom_S = right_W * right_H_bottom

        A = [left_S, right_top_S, right_bottom_S]
        score = max(A) - min(A)
        if score < min_score:
            min_score = score
    return min_score

def horizontal_and_vertical_cut(H, W):
    return vertical_and_horizontal_cut(W, H)

a = vertical_cut(H, W)
b = horizontal_cut(H, W)
c = vertical_and_horizontal_cut(H, W)
d = horizontal_and_vertical_cut(H, W)

print(min(a, b, c, d))
