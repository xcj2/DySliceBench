# -*- coding: utf-8 -*-

import math

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
    else:
        debug = True
        lines = [e for e in lines_as_string.split("\n")][1:-1]
    
    token = lines[0].split(" ")
    n = int(token[0])
    a = [int(i) for i in lines[1].split(" ")]
    b = [int(i) for i in lines[2].split(" ")]

    return (n, a, b)


def solve(n, a, b):
    
    result = 0
    for i in range(n):
        
        if a[i] >= b[i]:
            c = b[i]
            e = 0
            a[i] = a[i] - c
        else:
            c = a[i]
            d = b[i] - c
            a[i] = 0
            if a[i+1] >= d:
                e = d
                a[i+1] = a[i+1] - d
            else:
                e = a[i+1]
                a[i+1] = 0
        
        result = result + (c+e)

    return result


def main():
    # 出力

    print("%s" % solve(*parse_input()))


if __name__ == '__main__':

    main()
