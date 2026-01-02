#-*- coding: utf-8 -*-
"""
oj dl https://atcoder.jp/contests/abc116/tasks/abc116_d -d test-d
oj test -d test-d -c "python abc116d.py"
oj test -d test-d -c "python abc116d.py" test-d/sample-3.in
"""
from collections import defaultdict
import sys
import math
from datetime import datetime
import re


def sol_lte(n, S):
    maxi = 0

    for i in range(n):
        tmp = 0
        for j in range(i, n):
            if j + 1 <= n -1:
                if S[j+1] <= S[j]:
                    tmp += 1
                else:
                    break
        maxi = max(maxi, tmp)
    return maxi


def sol(n, S):
    maxi = 0 # steps
    tmp = 0
    for i in range(1, n):
        if S[i] <= S[i-1]:
            tmp += 1
            maxi = max(maxi, tmp)
        else:
            tmp = 0

    return maxi


do_submit = True
#do_submit = False

def input_parse(input_str):
    lines = [x.strip() for x in input_str.split("\n") if x.strip()]
    parsed_lines = [list(map(str, line.split())) for line in lines]
    #print(parsed_lines)
    n = int(parsed_lines[0][0])
    k = int(parsed_lines[0][1])
    #S = parsed_lines[0][0]
    return n, k


if not do_submit:
    n, k = input_parse("""
    5
10 4 8 7 3
    """)
    print(sol(n, k))

    n, k = input_parse("""
    100000 5
    """)
    print(sol(n, k))


else:
    n = int(input().strip())
    S = list(map(int, input().split()))
    #S = input()
    print(sol(n, S))

    # S = input().strip()
    # print(sol(S))



