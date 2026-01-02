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
#        for line in sys.stdin:
#            lines.append(line)
        lines.append(input())
        lines.append(input())
    else:
        debug = True
        lines = [e for e in lines_as_string.split("\n")][1:-1]

    n, k = [int(e) for e in lines[0].split(" ")]

    hs = [int(e) for e in lines[1].split(" ")]

    return (n, k, hs)


def solve(n, k, hs):


    result = len([h for h in hs if h >= k])

    return result


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
	