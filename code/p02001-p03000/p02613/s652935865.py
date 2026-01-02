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

    n = int(lines[0])
    ss = lines[1:]

    return (n, ss)


def solve(n, ss):


    d = dict()
    for i in range(n):
        s = ss[i]
        cnt = d.get(s, 0)
        cnt = cnt + 1
        d[s] = cnt

    result = []
    for e in ['AC', 'WA', 'TLE', 'RE']:
        result.append("%s x %d " % (e, d.get(e, 0)))
    
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
	