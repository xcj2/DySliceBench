# -*- coding: utf-8 -*-

import sys

def parse_input(lines_as_string = None):


    lines = []
    if lines_as_string is None:
        lines.append(input())
        lines.append(input())
        lines.append(input())
        lines.append(input())
        lines.append(input())
        lines.append(input())
    else:
        lines = [e for e in lines_as_string.split("\n")][1:-1]


    a_e = [int(e) for e in lines[:5]]
    k = int(lines[5])

    return (a_e, k)


def solve(a_e, k):

    result = False
    for i in range(5):
        for j in range(i+1, 5):
            if a_e[j] - a_e[i] > k:
                result = True
                break

        if result:
            break
    if result:
        res = ':('
    else:
        res = 'Yay!'           

    return res 


def main():
    # 出力

    print("%s" % solve(*parse_input()))

if __name__ == '__main__':

    main()
