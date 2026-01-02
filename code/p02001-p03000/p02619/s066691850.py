#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def input():
    return sys.stdin.readline()


def down_pleasure(c_list, day_num, contest_last_day):
    """その日の満足度低下を返す"""
    sum_down_pl = 0
    for i in range(26):
        sum_down_pl += c_list[i] * (day_num - contest_last_day[i])

    return sum_down_pl


def calc_pleasure(s_list, t_list, d, c_list, contest_last_day):
    pleasure = 0

    for day, t_num in zip(range(d), t_list):
        pleasure += s_list[day][t_num-1]
        contest_last_day[t_num-1] = day + 1
        pleasure -= down_pleasure(c_list, day+1, contest_last_day)
        print(pleasure)

    return pleasure






def resolve():
    d = int(input().rstrip())
    c_list = list(map(int, input().split()))
    s_list = [list(map(int, input().split())) for i in range(d)]
    t_list = []

    for i in range(d):
        t_list.append(int(input().rstrip()))

    contest_last_day = []
    for i in range(26):
        contest_last_day.append(0)

    pleasure = calc_pleasure(s_list, t_list, d, c_list, contest_last_day)




if __name__ == "__main__":
    resolve()

