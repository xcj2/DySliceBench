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
        lines.append(input())
    else:
        debug = True
        lines = [e for e in lines_as_string.split("\n")][1:-1]


    t = [int(c) for c in lines[0]]

    return (t, )


def solve(t, ):

    if debug:
        log("t=%s" % t)
    
    tmp = []
    for e in t:
        if e == 0:
            tmp.append(False)
        else:
            tmp.append(True)
    
    result = 0
    if len(t) == 1:
        pass
    else:
        for i in range(1, len(tmp)):
            if tmp[i-1] == tmp[i]:
                tmp[i] = not tmp[i-1]
                result = result + 1
        # while True:
        #     if debug:
        #         log("tmp=%s" % tmp)
        #     result_tmp = result
        #     for i in range(1, len(tmp)):
        #         if tmp[i-1] == tmp[i]:
        #             tmp[i] = not tmp[i-1]
        #             result = result + 1
        #             break
        #     if result_tmp == result:
        #         break
                

    return result


def main():
    # 出力

    print("%s" % solve(*parse_input()))

if __name__ == '__main__':

    main()
