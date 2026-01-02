# -*- coding: utf-8 -*-

import sys
import math
import itertools

debug = False

def log(text):
    if debug:
        print(text)


def parse_input(lines_as_string = None):

    global debug
    lines = []
    if lines_as_string is None:
        debug = False
        lines.append(input())
        (n, m, x) = [int(e) for e in lines[0].split(' ')]
        for _ in range(n):
            lines.append(input())
    else:
        debug = True
        lines = [e for e in lines_as_string.split("\n")][1:-1]
        (n, m, x) = [int(e) for e in lines[0].split(' ')]

    ca_list = []
    for i in range(1, n+1):
        ca_list.append([int(e) for e in lines[i].split(' ')])
        
    return (n, m, x, ca_list)


def solve(n, m, x, ca_list):


    result = 100000 * n + 1
    for p in itertools.product([0,1], repeat=n):

        index_set = set([i for i, b in enumerate(p) if b == 1])
        ca_list_tmp = [e for i, e in enumerate(ca_list) if i in index_set]

        if debug:
            log("index_set=%s" % index_set)
            log("ca_list_tmp=%s" % ca_list_tmp)
        
        total_c = 0
        total_a = [0 for _ in range(m)]
        r = True 
        for ca in ca_list_tmp:
            total_c = total_c + ca[0]

            for i in range(1, m + 1):
                total_a[i-1] = total_a[i-1] + ca[i]

        for i in range(m):
            if total_a[i] < x:
                r = False
                break
            
        if r:
            if total_c < result:
                result = total_c

    if result == 100000 * n + 1:
        result = -1

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