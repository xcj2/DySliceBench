# -*- coding: utf-8 -*-
"""
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0074
"""
import sys


def calc_remaining_second(hh, mm, ss):
    elapsed = (hh*3600) + (mm*60) + ss
    return (3600*2) - elapsed


def prettify_second(s, mode='normal'):
    if mode == 'long':
        s *= 3
    hh = s // 3600
    s %= 3600
    mm = s // 60
    s %= 60
    ss = s
    return '{:02d}:{:02d}:{:02d}'.format(hh, mm, ss)



def main(args):
    while True:
        hh, mm, ss = [int(x) for x in input().strip().split(' ')]
        if hh == -1 and mm == -1 and ss == -1:
            break
        remaining_sec = calc_remaining_second(hh, mm, ss)
        print(prettify_second(remaining_sec, 'normal'))
        print(prettify_second(remaining_sec, 'long'))


if __name__ == '__main__':
    main(sys.argv[1:])