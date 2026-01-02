# -*- coding: utf-8 -*-

import sys
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
        for line in sys.stdin:
            lines.append(line.strip())
    else:
        debug = True
        lines = [e for e in lines_as_string.split("\n")][1:-1]

    s = lines[0]
    

    return (s, )


def solve(s):

    result = s
    if s[-1] == 's':
        result = result + 'es'
    else:
        result = result + 's'

    return result
    


def main():
    # 出力
    result = solve(*parse_input())
    if isinstance(result, list):
        for r in result:
            print("%s" % r, sep='')
    else:
        print("%s" % result, sep='')

if __name__ == '__main__':

    main()
	