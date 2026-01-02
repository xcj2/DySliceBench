# -*- coding: utf-8 -*-
"""
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0110
"""
# runtime error
import sys
import re

def solve(exp):
    p1 = re.compile('^0+')
    for i in range(10):
        modified_exp = exp.replace('X', str(i))
        left, right = modified_exp.split('=')
        left1, left2 = left.split('+')

        left1 = p1.sub('', left1)
        if left1 == '':
            left1 = '0'
        left2 = p1.sub('', left2)
        if left2 == '':
            left2 = '0'
        right = p1.sub('', right)
        if right == '':
            right = '0'

        # print('{} + {} <=> {}'.format(left1, left2, right))
        if int(left1) + int(left2) == int(right):
            return i
    return 'NA'



def solve2(exp):
    for i in range(10):
        left, right = exp.split('=')
        left1, left2 = left.split('+')

        left1 = left1.replace('X', str(i))
        left2 = left2.replace('X', str(i))
        right = right.replace('X', str(i))
        if len(left1) > 1 and left1[0] == '0':
            continue
        if len(left2) > 1 and left2[0] == '0':
            continue
        if len(right) > 1 and right[0] == '0':
            continue
        if int(left1, base=10) + int(left2, base=10) == int(right, base=10):
            return i
    return 'NA'




def main(args):
    for line in sys.stdin:
        #result = solve(line.strip())
        #print(result)
        result = solve2(line.strip())
        print(result)


if __name__ == '__main__':
    main(sys.argv[1:])