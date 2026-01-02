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

    n = [int(e) for e in lines[0].split(" ")][0]
    s = lines[1]

    return (n, s)


def solve(n, s):

    
    last = None
    result = []
    for i in range(n):
        if s[i] != last:
            result.append(s[i])
        last = s[i]


    if debug:
        log("result=%s" % result)
        
    return len(result) 


def main():
    # 出力
    result = solve(*parse_input())
    if isinstance(result, list):
        for r in result:
            print("%s" % r, end=' ')
    else:
        print("%s" % result)

if __name__ == '__main__':

    main()
	