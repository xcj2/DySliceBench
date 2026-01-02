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

def count1(bits):
    counter = 0
    while bits > 0:
        if bits & 1:
            counter += 1
        bits >>= 1
    return counter

def sol(N, testimonies):
    # print(N)
    # print(testimonies)
    maxi = 0
    for i in range(1<<N):
        ok = True
        for j in range(N):
            for x, y in testimonies[j]:
                if i & (1 << j): #正直者
                    if i & (1 << (x-1)) and not y: # 正直者と行っており、そうじゃないやん
                        ok = False; break
                    elif not (i & (1 << (x-1))) and y: #嘘つきといってるけど、そうじゃないやん！
                        ok = False; break
            if not ok:
                break
        if ok:
            maxi = max(count1(i), maxi)
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
    N = int(input().strip())
    testimonies = []
    for i in range(N):
        A = int(input().strip())
        XYs = []
        for j in range(A):
            x, y = list(map(int, input().split()))
            XYs.append((x, y))
        testimonies.append(XYs)
    #S = input()
    print(sol(N, testimonies))

    # S = input().strip()
    # print(sol(S))



