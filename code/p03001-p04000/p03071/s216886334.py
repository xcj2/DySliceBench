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
    else:
        debug = True
        lines = [e for e in lines_as_string.split("\n")][1:-1]


    token = lines[0].split()
    a = int(token[0])
    b = int(token[1])

    return (a, b)


def solve(a, b):

    if debug:
        log("a=%s" % a)
        log("b=%s" % b)
        
    tmp_a = a
    tmp_b = b

    result = 0
    for i in range(2):
        if tmp_a > tmp_b:
            result = result + tmp_a
            tmp_a = tmp_a - 1
        else:
            result = result + tmp_b
            tmp_b = tmp_b - 1

    return result


def main():
    # 出力

    print("%s" % solve(*parse_input()))

if __name__ == '__main__':

    main()
	