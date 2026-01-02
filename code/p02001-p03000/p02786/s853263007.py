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
    else:
        debug = True
        lines = [e for e in lines_as_string.split("\n")][1:-1]
    


    h = int(lines[0])

    return (h, )

def solve(h, ):

    current_h = h
    total_count = 1
    current_count = 1
    while True:
        
        if current_h == 1:
            break

        current_h = current_h // 2
        current_count = 2 * current_count
        total_count = total_count + current_count


    result = total_count 

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
	