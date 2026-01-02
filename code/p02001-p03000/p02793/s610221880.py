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
import math
#sys.setrecursionlimit(314159265)

def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a


def lcm(a,b):
    return a*b//gcd(a,b)

def lcm_list(nums):
    if len(nums) == 0:
        return None
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        lcm(nums[0], nums[1])
    else: # > 2
        a = lcm(nums[0], nums[1])
        for i in range(2, len(nums)):
            A = lcm(a, nums[i])
            a = A
        return a




def sol(S):
    mod = 10**9 + 7
    x = lcm_list(S)
    #print(x)
    T = [ x//s for s in S]
    return sum(T) % mod







do_submit = True
#do_submit = False

def input_parse(input_str):
    lines = [x.strip() for x in input_str.split("\n") if x.strip()]
    parsed_lines = [list(map(str, line.split())) for line in lines]
    print(parsed_lines)
    # n = int(parsed_lines[0][0])
    # k = int(parsed_lines[0][1])
    S = parsed_lines[0][0]
    return S


if not do_submit:
    S = input_parse("""
    1905
    """)
    print(sol(S))

    S = input_parse("""
    0112
    """)
    print(sol(S))

    S = input_parse("""
    1700
    """)
    print(sol(S))

    S = input_parse("""
    0000
    """)
    print(sol(S))

    S = input_parse("""
    1001
    """)
    print(sol(S))



else:
    n = int(input())
    S = list(map(int, input().split()))
    #S = input()
    print(sol(S))

    # S = input().strip()
    # print(sol(S))
    # print(lcm(2, 3))
    # print(lcm_list([2, 3, 4]))
    # print(lcm_list([27, 9, 3]))




