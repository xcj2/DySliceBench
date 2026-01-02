# -*- coding: utf-8 -*-

import sys

def parse_input(lines_as_string = None):


    lines = []
    if lines_as_string is None:
        lines.append(input())
    else:
        lines = [e for e in lines_as_string.split("\n")][1:-1]
 
    tokens = lines[0].split(" ")
    a = int(tokens[0])
    b = int(tokens[1])
    c = int(tokens[2])

    return (a, b, c)


def solve(a, b, c):

    tmp = b
    count = 0
    while True:
        tmp = tmp - a
        if tmp >= 0:
            count += 1
        else:
            break

        if count >= c:
            break

    return count

def main():
    # 出力

    print("%s" % solve(*parse_input()))

if __name__ == '__main__':

    main()
