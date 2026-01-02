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

    s = lines[0]

    return (s, )


def solve(s, ):

    n = len(s)
    ma = (n - 1) // 2 
    mb = (n + 3) // 2

    def test_text(text):
        if debug:
            log("text=%s" % text)
        n = len(text) 
        m = (n - 1) // 2
        result = True
        for i in range(m+1):
            if debug:
                log('(s[%d], s[%d])=(%s, %s)' % (i, -(i+1), s[i], s[-(i+1)]))
            if text[i] != text[-(i+1)]:
                result = False
                break

        return result

    if debug:
        log("s =%s" % s)
        log("ma=%d, sa=%s" % (ma, s[:ma]))
        log("mb=%d, sb=%s" % (mb, s[mb-1:]))

    result1 = test_text(s) 
    result2 = test_text(s[:ma]) 
    result3 = test_text(s[mb-1:]) 
    if debug:
        log('result1=%s, result2=%s, result3=%s' % (result1, result2, result3))

    result  = 'No'
    if result1 and result2 and result3:
        result = 'Yes'


    
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