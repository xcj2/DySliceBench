#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def input():
    return sys.stdin.readline()

def dfs_four_number(s_num, i, op_list:list):
    # ベースケース
    if i == 3:
        ans_num = int(s_num[0])
        for j, op in enumerate(op_list):
            if op == "+":
                ans_num += int(s_num[j+1])
            elif op == "-":
                ans_num -= int(s_num[j+1])

        if ans_num == 7:
            return op_list
        else:
            return False

    op_list.append("+")
    if dfs_four_number(s_num, i+1, op_list):
        return op_list

    op_list.pop()
    op_list.append("-")
    if dfs_four_number(s_num, i+1, op_list):
        return op_list
    op_list.pop()



def resolve():
    s_num = input().rstrip()

    op_list = []
    ans_op_list = dfs_four_number(s_num, 0, op_list)

    ans_str = ""
    for s, op in zip(s_num, ans_op_list):
        ans_str += s
        ans_str += op

    ans_str += s_num[3] + "=7"
    print(ans_str)

if __name__ == "__main__":
    resolve()

