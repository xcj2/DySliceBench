# -*- coding: utf-8 -*-
"""
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0128

"""
import sys
from sys import stdin
input = stdin.readline


def conv_avacus(num_txt):
    abacus = ['* = ****', '* =* ***', '* =** **', '* =*** *', '* =**** ',
              ' *= ****', ' *=* ***', ' *=** **', ' *=*** *', ' *=**** ']
    ans = [abacus[int(num_txt[4])], abacus[int(num_txt[3])], abacus[int(num_txt[2])], abacus[int(num_txt[1])], abacus[int(num_txt[0])]]
    return ans


def rotate_and_print(data):
    y_size = len(data)
    x_size = len(data[0])
    A = [[''] * y_size for _ in range(x_size)]
    for i in range(x_size):
        for j in range(y_size):
            A[i][j] = data[y_size-1-j][i]

    for l in A:
        print(''.join(l))


def main(args):
    first_case = True
    for line in sys.stdin:
        if not first_case:
            print()
        num_txt = line.strip().zfill(5)
        result = conv_avacus(num_txt)
        rotate_and_print(result)
        first_case = False


if __name__ == '__main__':
    main(sys.argv[1:])
    