# -*- coding: utf-8 -*-

import sys

def parse_input(lines_as_string = None):


    lines = []
    if lines_as_string is None:
        lines.append(input())
    else:
        lines = [e for e in lines_as_string.split("\n")][1:-1]

    tokens = lines[0].split(" ")
    a, b, c = tokens

    return (a, b, c)


def solve(a, b, c):
    
    result = "No"
    if a + b > c and b + c > a and c + a > b:
        result = "Yes"

    return result

def main():
    # 出力

    print("%s" % solve(*parse_input()))

if __name__ == '__main__':

    main()
