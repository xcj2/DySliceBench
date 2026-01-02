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
        # for line in sys.stdin:
        #     lines.append(line)
        lines.append(input())
        n = int(lines[0])
        for _ in range(n):
            lines.append(input())
    else:
        debug = True
        lines = [e for e in lines_as_string.split("\n")][1:-1]
        n = int(lines[0])
    
    s = lines[1:]


    return (n, s)


def solve(n, s):

    d = dict() 
    max_cnt = 0
    for i in range(n):
        cnt = d.get(s[i], 0)
        cnt = cnt + 1
        d[s[i]] = cnt
        if cnt > max_cnt:
            max_cnt = cnt

    result = []
    for word, cnt in d.items():    
        if cnt == max_cnt:
            result.append(word)

    result.sort()

    return  result


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