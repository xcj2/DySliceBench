# -*- coding: utf-8 -*-

import sys
import math

debug = False

def log(text):
    if debug:
        print(text)

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr


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
    

    n = int(lines[0])

    return (n, )


def solve(n):

    if n == 1:
        return 0

    factors = factorization(n) 

    result = 0
    for f in factors:
        p = f[0]
        e = f[1]

        m = 0 
        for i in range(1, 1000):

            s = i * (i + 1) // 2
            if s > e:
                m = i - 1
                break

        if debug:
            log("p=%d, e=%d, m=%d" % (p, e, m))

        result = result + m
       

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
