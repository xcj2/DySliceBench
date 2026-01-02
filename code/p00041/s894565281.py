# -*- coding: utf-8 -*-
"""
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0041
"""
import sys
from itertools import permutations, product


def make_ten(digits):
    result = '0'
    for a, b, c, d in permutations(digits, 4):
        if result != '0':
            break
        for op1, op2, op3 in product(['+', '-', '*'], repeat=3):
            # 1, 2, 3
            exp = '((({} {} {}) {} {}) {} {})'.format(a, op1, b, op2, c, op3, d)
            if eval(exp) == 10:
                result = exp
                break
            # 1, 3, 2
            exp= '(({} {} {}) {} ({} {} {}))'.format(a, op1, b, op2, c, op3, d)
            if eval(exp) == 10:
                result = exp
                break
            # 2, 1, 3
            exp = '(({} {} ({} {} {})) {} {})'.format(a, op1, b, op2, c, op3, d)
            if eval(exp) == 10:
                result = exp
                break
            # 3, 1, 2
            exp = '({} {} (({} {} {}) {} {}))'.format(a, op1, b, op2, c, op3, d)
            if eval(exp) == 10:
                result = exp
                break
            # 3, 2, 1
            exp = '({} {} ({} {} ({} {} {})))'.format(a, op1, b, op2, c, op3, d)
            if eval(exp) == 10:
                result = exp
                break
            # 2, 3, 1
            exp =  '(({} {} {}) {} ({} {} {}))'.format(a, op1, b, op2, c, op3, d)
            if eval(exp) == 10:
                result = exp
                break
    return result


# ????????°????????????????????????10?????????????????????????????¢?????°????????§?????????????????????????????°??????????????¨???????????????????????¨??????????´????????????????
Memo = {}
def solve(digits):
    global Memo
    digits.sort(reverse=True)
    data = ''.join(map(str, digits))
    if data in Memo:
        pass
    else:
        Memo[data] = make_ten(digits)
    return Memo[data]


def main(args):
    while True:
        digits = [int(x) for x in input().strip().split(' ')]
        # digits = [int(x) for x in '{:04d}'.format(count)]
        if digits[0] == 0 and digits[1] == 0 and digits[2] == 0 and digits[3] == 0:
            break
        result = solve(digits)
        print(result)
        #print('count={}, {}'.format(count, result))


if __name__ == '__main__':
    main(sys.argv[1:])