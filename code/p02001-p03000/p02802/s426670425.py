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
        (n, m) = [int(e) for e in lines[0].split(" ")]
        for _ in range(m):
            lines.append(input())
    else:
        debug = True
        lines = [e for e in lines_as_string.split("\n")][1:-1]
        (n, m) = [int(e) for e in lines[0].split(" ")]


    ps = [] 
    for i in range(1, m + 1):
        e = lines[i].split(" ")
        p = int(e[0])
        s = e[1]
        ps.append((p, s))

    return (n, m, ps)


def solve(n, m, ps):

    
    submits = dict()
    # for i in range(1, n+1):
    #     submits[i] = []

    for (p, s) in ps:

        ans_list = submits.get(p, [])
        ans_list.append(s)
        submits[p] = ans_list
    
    total_ac = 0
    total_wa = 0
    for (p, ans_list) in submits.items():

        ac = 0
        wa = 0
        for ans in ans_list:
            if ans == 'WA':
                wa = wa + 1
            elif ans == 'AC':
                ac = ac + 1
                break
        
        if ac == 0:
            wa = 0

        total_ac = total_ac + ac
        total_wa = total_wa + wa
        
        if debug:
            log("p=%d, ac=%d, wa=%d" % (p, ac, wa))
            log("total_ac=%d, total_wa=%d" % (total_ac, total_wa))

    result = [total_ac, total_wa] 

    return result


def main():
    # 出力
    result = solve(*parse_input())
    if isinstance(result, list):
        print("%d %d" % (result[0], result[1]))
    else:
        print("%s" % result, sep='')

if __name__ == '__main__':

    main()