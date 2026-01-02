# -*- coding: utf-8 -*-

import sys

debug = False

def log(text):
    if debug:
        print(text)

def parse_input(lines_as_string = None):

    global debug
    lines = []
    if lines_as_string is None:
        debug = False
        lines.append(input())
        lines.append(input())
        lines.append(input())
        lines.append(input())

    else:
        debug = True
        lines = [e for e in lines_as_string.split("\n")][1:-1]

    n = int(lines[0])

    a = [int(e) for e in lines[1].split(" ")]
    b = [int(e) for e in lines[2].split(" ")]
    c = [int(e) for e in lines[3].split(" ")]

    return (n, a, b, c)


def solve(n, a, b, c):

    total = 0
    previous_dish_num = -1
    for i in range(n):
        dish_num = a[i]
        total = total + b[dish_num-1]
        if previous_dish_num + 1 == dish_num:
            total = total + c[previous_dish_num-1]
        previous_dish_num = dish_num

    return total


def main():
    # 出力
    result = solve(*parse_input())
    if isinstance(result, list):
        for r in result:
            print("%s" % r)
    else:
        print("%s" % result)

if __name__ == '__main__':

    main()
	