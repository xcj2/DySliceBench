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

    (n, d) = [int(e) for e in lines[0].split(' ')]
    xy = []
    for i in range(1, n+1):
        tmp = lines[i].split(' ')
        xy.append((int(tmp[0]), int(tmp[1])))

    return (n, d, xy)


def solve(n, d, xy):

    result = 0
    for i in range(n):
      x = xy[i][0]
      y = xy[i][1]
      if x * x + y * y <= d * d:
          result = result + 1

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
	