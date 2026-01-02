#-*- coding: utf-8 -*-
"""
oj dl https://atcoder.jp/contests/abc116/tasks/abc116_d -d test-d
oj test -d test-d -c "python abc116d.py"
oj test -d test-d -c "python abc116d.py" test-d/sample-3.in
"""
from collections import defaultdict
import sys
import math



def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a % b)

def sol(a, b, k):
    D = []
    for i in range(1, min(a, b)+1):
        if a % i == 0 and b % i == 0:
            D.append(i)
    D.reverse()
    return D[k-1]



do_submit = True
#do_submit = False
def input_parse(input_str):
    lines = [x.strip() for x in input_str.split("\n") if x.strip()]
    parsed_lines = [list(map(int, line.split())) for line in lines]
    a, b, c = parsed_lines[0]
    return a, b, c


if not do_submit:
    a, b, c = input_parse("""
    8 12 2
    """)
    print(sol(a, b, c))
    a, b, c = input_parse("""
    100 50 4
    """)
    print(sol(a, b, c))
    a, b, c = input_parse("""
    1 1 1
    """)
    print(sol(a, b, c))
else:
    a, b, k = list(map(int, input().split()))
    print(sol(a, b, k))
    # S = []
    # for i in len(n):
    #     S.append(int(input().strip()))
    #print(sol(n, a, b, c, S))

