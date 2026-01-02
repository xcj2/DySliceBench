# -*- coding: utf-8 -*-

import sys
import math
from decimal import Decimal, ROUND_DOWN
from collections import deque
from itertools import combinations
import copy

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

    (h, w, k) = [int(e) for e in lines[0].split(' ')]
    cs = []
    for i in range(1, h+1):
        l = [ c for c in lines[i]]
        cs.append(l)


    return (h, w, k, cs)


def solve(h, w, k, cs):


    def count_black(cs):
        return sum([len([ e for e in c if e == '#']) for c in cs])

    def gen_index(n):
        result = []
        for i in range(n+1):
            combs = combinations(range(n), i)
            for cb in combs:
                result.append(cb)
        return result

    cnt = 0
    for r in gen_index(h):
        for c in gen_index(w):
            ds = copy.deepcopy(cs)
            if debug:
                log("ds=%s" % ds)

            for i in range(h):
                for j in range(w):
                    if i in r or j in c:
                        ds[i][j] = 'R'

            
            cnt_black = count_black(ds)
            if cnt_black == k:
                if debug:
                    log("r=%s" % (r,))
                    log("c=%s" % (c,))
                    log("ds=%s" % ds)
                    log("cnt_black=%d" % cnt_black)
                cnt = cnt + 1


    return cnt
    


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
	
