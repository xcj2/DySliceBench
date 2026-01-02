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

    result = b
    if 13 <= a:
        result = b
    elif 6 <= a and a <= 12:
        result = int(b/2)
    else:
        result = 0
        
    return result




def main():
    # 出力

    print("%s" % solve(*parse_input()))

if __name__ == '__main__':

    main()
	