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
        for i in range(n):
            lines.append(input())
        lines.append(input())
    else:
        debug = True
        lines = [e for e in lines_as_string.split("\n")][1:-1]
        n = int(lines[0])
    
    st = []
    for i in range(1, n+1):
        (s, t) = lines[i].split(" ")
        st.append((s, int(t)))
    x = lines[n+1]

    return (n, st, x)


def solve(n, st, x):

    index = None
    for i in range(n):
        (s, _) = st[i]
        if s == x:
            index = i
    
    st2 = st[index + 1:]
    result = sum([e[1] for e in st2])

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
	