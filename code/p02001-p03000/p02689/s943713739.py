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
        lines.append(input())
        (n, m) = [int(e) for e in lines[0].split(' ')]
        lines.append(input())
        for _ in range(m):
            lines.append(input())
    else:
        debug = True
        lines = [e for e in lines_as_string.split("\n")][1:-1]
        (n, m) = [int(e) for e in lines[0].split(' ')]

    h_list = [int(e) for e in lines[1].split(' ')]
    ab_list = []
    for i in range(2, m+2):
        ab_list.append([int(e) for e in lines[i].split(' ')])
        
    return (n, m, h_list, ab_list)


def solve(n, m, h_list, ab_list):


    bad_tower = set()
    for j in range(m):

        ab = ab_list[j]
        if h_list[ab[0]-1] <= h_list[ab[1]-1]:
            bad_tower.add(ab[0])
        
        if h_list[ab[1]-1] <= h_list[ab[0]-1]:
            bad_tower.add(ab[1])

        if debug:
            log("j=%d, bad_tower=%s" % (j, bad_tower))
    
    result = n - len(bad_tower)

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