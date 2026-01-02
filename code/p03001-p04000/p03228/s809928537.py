# -*- coding: utf-8 -*-
# !/usr/bin/env python
# vim: set fileencoding=utf-8 :

"""
#
# Author:   Noname
# URL:      https://github.com/pettan0818
# License:  MIT License
# Created: 土 10/27 21:08:25 2018

# Usage
#
"""
def get():
    return [int(i) for i in input().split(' ')]

def emurate_process(takahashi, aoki, mode):
    if mode == 't':
        hero = takahashi
        opposite = aoki
    else:
        hero = aoki
        opposite = takahashi

    if hero % 2 == 1:
        hero -= 1
    watasu = hero // 2
    hero = watasu
    opposite += watasu

    if mode == 't':
        return hero, opposite
    else:
        return opposite, hero


def solve(A,B,K):
    for i in range(K):
        if i % 2 == 0:  # takahashi is hero.
            A, B = emurate_process(A, B, 't')
        elif i % 2 == 1:  # aoki is hero.
            A, B = emurate_process(A, B, 'a')

    print('{} {}'.format(int(A),int(B)))

if __name__ == '__main__':
    solve(*get())

