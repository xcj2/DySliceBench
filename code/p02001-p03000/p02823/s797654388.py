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
    else:
        debug = True
        lines = [e for e in lines_as_string.split("\n")][1:-1]

    (n, a, b) = [int(e) for e in lines[0].split(" ")]

    return (n, a, b)

def solve(n, a, b):
 

    c = b - a 
    d = c // 2
    result1 = 0
    if c % 2 == 0:
        result_p = min([b-1, n-a, d])
    else:
        result_p = min([b-1, n-a])

    game_count_1 = a - 1
    a_idx = 1
    b_idx = b - game_count_1
    dist = b_idx - a_idx
    result_q = 0
    if dist % 2 == 0:
        game_count_2 = dist // 2
        result_q = game_count_1 + game_count_2 
    else:
        dist = (b_idx - 1) - a_idx
        game_count_2 = dist // 2
        result_q = game_count_1 + 1 + game_count_2 


    game_count_3 = n - b
    a_idx = a + game_count_3
    b_idx = n
    dist = b_idx - a_idx
    result_r = 0
    if dist % 2 == 0:
        game_count_4 = dist // 2
        result_r = game_count_3 + game_count_4
    else:
        dist = b_idx - (a_idx + 1)
        game_count_4 = dist // 2
        result_r = game_count_3 + 1 + game_count_4



    result = min([result_p, result_q, result_r])

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
	