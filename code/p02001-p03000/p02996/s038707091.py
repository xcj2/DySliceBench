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
        tokens = lines[0].split(" ")
        n = int(tokens[0])
        for i in range(n):
            lines.append(input())
    else:
        debug = True
        lines = [e for e in lines_as_string.split("\n")][1:-1]
        tokens = lines[0].split(" ")
        n = int(tokens[0])

    ab_list = []
    for i in range(1, n+1):
        tokens = lines[i].split(" ")
        a = int(tokens[0])
        b = int(tokens[1])
        ab_list.append((a, b))

    return (n, ab_list)


def solve(n, ab_list):


    ab_list.sort(key = lambda e: e[1])

    sum = 0
    result = "Yes"
    for i in range(n):
        e = ab_list[i]
        sum = sum + e[0]
        if sum > e[1]:
            result = "No"
            break

    return result


def main():
    # 出力

    print("%s" % solve(*parse_input()))

if __name__ == '__main__':

    main()
