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
    t = lines[1]

    return (s, t)


def solve(s, t):


    n = len(t) 
    count = n
    for i in range(len(s) - len(t) + 1):
        tmp_s = s[i:i+n]
        
        cnt = 0
        for j in range(n):
            if tmp_s[j] != t[j]:
                cnt = cnt + 1

        if cnt < count:
            count = cnt 


    return count


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
	