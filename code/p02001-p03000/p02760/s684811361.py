#!/usr/bin/env python3

import sys

DEBUG = False

def solve():
    return


def read_int_list(sep = " "):
    return [int(s) for s in sys.stdin.readline().rstrip().split(sep)]

def read_int():
    return int(sys.stdin.readline())

def dprint(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)
    return

def printbingo(bingo):
    if not DEBUG:
        return
    for y in range(0, 3):
        for x in range(0, 3):
            print(bingo[y][x], end=" ")
        print()


def main():
    bingo = [[]] * 3
    bingo[0] = read_int_list()
    bingo[1] = read_int_list()
    bingo[2] = read_int_list()
    locs = {}
    for y in range(0, 3):
        for x in range(0, 3):
            locs[bingo[y][x]] = (y, x)
    printbingo(bingo)
            
    n = read_int()
    for _ in range(0, n):
        b = read_int()
        if b in locs:
            bingo[locs[b][0]][locs[b][1]] = -1
    printbingo(bingo)
    
    # column check
    for y in range(0, 3):
        is_bingo = True
        for x in range(0, 3):
            if bingo[y][x] != -1:
                is_bingo = False
                break
        if is_bingo:
            print("Yes")
            return
    # row check
    for x in range(0, 3):
        is_bingo = True
        for y in range(0, 3):
            if bingo[y][x] != -1:
                is_bingo = False
                break
        if is_bingo:
            print("Yes")
            return
    # cross check
    for (y, x), (dy, dx) in [((0, 0), (1, 1)), ((0, 2), (1, -1))]:
        is_bingo = True
        while is_bingo and 0 <= y < 3 and 0 <= x < 3:
            #dprint(f"(x,y):{(x, y)}, (dx,dy):{(dx,dy)}, bing[y][x]: {bingo[y][x]}")
            if bingo[y][x] != -1:
                is_bingo = False
                break
            y += dy
            x += dx
        if is_bingo:
            print("Yes")
            return
    print("No")


if __name__ == "__main__":
    main()