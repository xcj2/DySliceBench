import copy
import math
import time
import statistics
import math
import itertools
import bisect
import sys
from decimal import *
from collections import deque


def get_int():
    return int(input())

def get_string():
    return input()

def get_int_list():
    return [int(x) for x in input().split()]

def get_string_list():
    return input().split()

def get_int_multi():
    return map(int, input().split())

def get_string_char_list():
    return list(str(input()))

# print("{} {}".format(a, b))
# a_list = [0] * a
sys.setrecursionlimit(10 ** 6)

def main():
    start = time.time()

    h, w = get_int_list()
    sr, sc = get_int_list()
    er, ec = get_int_list()

    d = [[-1] * (w+2) for _ in range(h+2)]

    for i in range(h):
        wk = get_string()
        for ii in range(w):
            if wk[ii] == ".":
                d[i+1][ii+1] = 10 ** 6

    d[sr][sc] = 0
    q = deque([])
    q2 = deque([])
    q.append([sr,sc])
    q2.append([sr,sc])

    def idou(i,ii,cnt_mahou):
        if 1 <= i <= h and 1 <= ii <= w:
            if d[i][ii] == 10 ** 6:
                q.append([i, ii])
                d[i][ii] = cnt_mahou


    ans = -1
    flg = True
    finish = False
    while flg:
        flg = False
        while q:
            wk = q.popleft()
            q2.append(wk)

            i = wk[0]
            ii = wk[1]
            cnt_mahou = d[i][ii]

            idou(i - 1, ii, cnt_mahou)
            idou(i + 1, ii, cnt_mahou)
            idou(i, ii - 1, cnt_mahou)
            idou(i, ii + 1, cnt_mahou)

            if d[er][ec] != 10 ** 6:
                ans = d[er][ec]
                finish = True
                break

        if finish:
            break

        while q2:
            wk = q2.popleft()
            i = wk[0]
            ii = wk[1]
            # 魔法を使う
            for wk in range(-2, 3):
                for wk2 in range(-2, 3):
                    if abs(wk) + abs(wk2) > 1:
                        flg = True
                        idou(i + wk, ii + wk2, cnt_mahou + 1)

    print(ans)

    #print(time.time() - start)


if __name__ == '__main__':
    main()