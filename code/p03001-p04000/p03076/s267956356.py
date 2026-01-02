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
        lines.append(input())
    else:
        debug = True
        lines = [e for e in lines_as_string.split("\n")][1:-1]


    a_e = [int(e) for e in lines[:5]]

    return (a_e,)

def permutation(tmp):

    if len(tmp) == 0:
        return [[]]
    else:
        result = []
        for i in range(len(tmp)):
            head = tmp[i]
            tail = tmp[0:i] + tmp[i+1:]
            for r in permutation(tail):
                result.append([head] + r)
        return result

def solve(a_e):

    result = 130 * 5
    for r in permutation(a_e):
        if debug:
            log("r=%s" % r)
        total = 0
        for e in r[:4]:
            tmp = e + total
            m = tmp % 10
            if m == 0:
                total = tmp
            else:
                total = tmp + (10 - m)
            if debug:
                log("e=%d, tmp=%d, total=%s" % (e, tmp, total))
        total = total + r[4]
        if debug:
            log("total=%s" % total)

        if total < result:
            if debug:
                log("r=%s" % r)
            result = total
 
    return result

def main():
    # 出力

    print("%s" % solve(*parse_input()))

if __name__ == '__main__':

    main()
