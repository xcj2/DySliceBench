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
    else:
        debug = True
        lines = [e for e in lines_as_string.split("\n")][1:-1]

    s = lines[0]

    return (s, )


def solve(s, ):

    result = 'Yes'
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i] == 'R' or s[i] == 'U' or s[i] == 'D':
                pass
            else:
                result = 'No'

        if i % 2 == 1:
            if s[i] == 'L' or s[i] == 'U' or s[i] == 'D':
                pass
            else:
                result = 'No'


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
	