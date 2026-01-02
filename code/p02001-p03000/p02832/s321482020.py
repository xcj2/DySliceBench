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
#        for line in sys.stdin:
#            lines.append(line)
        lines.append(input())
        lines.append(input())
    else:
        debug = True
        lines = [e for e in lines_as_string.split("\n")][1:-1]

    n = [int(e) for e in lines[0].split(" ")][0]
    a = [int(e) for e in lines[1].split(" ")]

    return (n, a)

def solve(n, a):

    current_num = 1
    count = 0
    result = []
    for i in range(n):
        if a[i] != current_num:
            count = count + 1
        else:
            current_num = current_num + 1
            result.append(a[i])
    
    if debug:
        log("result=%s" % result)
        log("count=%s" % count)
    
    if result == []:
        count = -1

    for i in range(1, len(result) + 1):
        if result[i-1] != i:
            if debug:
                log("result[%d]=%s" % (i, result[i-1]))
            count = -1
            break


    return count

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
	