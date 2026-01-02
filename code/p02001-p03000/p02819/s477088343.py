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
        # error?
        # for line in sys.stdin:
        #     lines.append(line)
        lines.append(input())

    else:
        debug = True
        lines = [e for e in lines_as_string.split("\n")][1:-1]

    x = [int(e) for e in lines[0].split(" ")][0]

    return (x, )


def solve(x):

    primes = set()

    def is_prime(n):
        
        if n in primes:
            return True

        if n == 1:
            return False

        for k in range(2, int(math.sqrt(n)) + 1):
            if n % k == 0:
                return False
        
        primes.add(n)

        return True

    y = x
    result = 0
    while True:
        if is_prime(y):
            result = y
            break
        else:
            y = y + 1

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
